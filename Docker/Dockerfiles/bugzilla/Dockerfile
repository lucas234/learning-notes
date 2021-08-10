FROM perl:5.20
MAINTAINER liulucas
RUN apt-get update && apt-get install -y sudo apache2 vim wget libmysqld-dev libmysqlclient-dev
#RUN echo "mysql-server mysql-server/root_password password root" | debconf-set-selections 
#RUN echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections 
#RUN apt install -y -f mysql-server=5.7.33-1ubuntu18.04

#RUN sudo DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server=5.7
#RUN sudo mysql -h 127.0.0.1 -P 3306 -u root -e"UPDATE mysql.user SET password = PASSWORD('123456') WHERE user = 'root'"

RUN wget http://ftp.mozilla.org/pub/mozilla.org/webtools/bugzilla-5.0.6.tar.gz
RUN mkdir /var/www/html/bugzilla
RUN tar xf bugzilla-5.0.6.tar.gz -C /var/www/html/bugzilla --strip-components=1
RUN rm bugzilla-5.0.6.tar.gz
RUN sudo chown -R www-data:www-data /var/www/html/bugzilla

RUN cd /var/www/html/bugzilla && perl install-module.pl --all
RUN cpan -i Class::XSAccessor::Array Class::XSAccessor
RUN perl checksetup.pl
