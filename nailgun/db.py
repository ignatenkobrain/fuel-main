# -*- coding: utf-8 -*-

import web
from sqlalchemy.orm import scoped_session, sessionmaker
from api.models import engine


def load_db_driver(handler):
    web.ctx.orm = scoped_session(sessionmaker(bind=engine))
    try:
        return handler()
    except web.HTTPError:
        web.ctx.orm.commit()
        raise
    except:
        web.ctx.orm.rollback()
        raise
    finally:
        web.ctx.orm.commit()


def syncdb():
    from api.models import Base
    Base.metadata.create_all(engine)


def dropdb():
    from api.models import Base
    Base.metadata.drop_all(engine)


def flush():
    from api.models import Base
    session = scoped_session(sessionmaker(bind=engine))
    for table in reversed(Base.metadata.sorted_tables):
        session.execute(table.delete())
        session.commit()
