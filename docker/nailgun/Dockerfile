# fuel-nailgun
#
# Version     0.1

FROM fuel/centos
MAINTAINER Matthew Mosesohn mmosesohn@mirantis.com

WORKDIR /root

RUN rm -rf /etc/yum.repos.d/*;echo -e "[nailgun]\nname=Nailgun Local Repo\nbaseurl=http://$(route -n | awk '/^0.0.0.0/ { print $2 }'):_PORT_/os/x86_64/\ngpgcheck=0" > /etc/yum.repos.d/nailgun.repo;yum clean all;mkdir -p /opt/gateone/users/ANONYMOUS/ /var/log/nailgun
#Workaround for nailgun settings.yaml template
RUN mkdir -p /root/.ssh;chmod 700 /root/.ssh;touch /root/.ssh/id_rsa.pub;chmod 600 /root/.ssh/id_rsa.pub

ADD etc /etc
ADD start.sh /usr/local/bin/start.sh

RUN puppet apply --detailed-exitcodes -d -v /etc/puppet/modules/nailgun/examples/nailgun-only.pp; [[ $? == 0 || $? == 2 ]]
RUN mkdir -p /var/log/remote /var/www/nailgun

#clean everything up
RUN yum --quiet remove -y gcc-c++ --skip-broken

RUN echo -e "[nailgun]\nname=Nailgun Local Repo\nbaseurl=file:/var/www/nailgun/centos/x86_64\ngpgcheck=0" > /etc/yum.repos.d/nailgun.repo; yum clean all; chmod +x /usr/local/bin/start.sh

EXPOSE 8001
VOLUME ["/usr/share/nailgun/static", "/etc/nailgun"]
CMD /usr/local/bin/start.sh
