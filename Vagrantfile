# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_check_update = false

  # Use one of the below:
  config.vm.network "private_network", ip: "192.168.33.100"
  # config.vm.network "public_network"

  config.vm.synced_folder ".", "/home/vagrant/flask-rabbitmq"

  config.vm.provider "virtualbox" do |vb|
   vb.gui = false
   vb.memory = "1024"
  end

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    sudo apt-get update
    sudo apt-get -y upgrade
    sudo apt-get -y install rabbitmq-server python-virtualenv python-pip python3-dev supervisor nginx

    sudo rabbitmqctl add_vhost flask-rabbitmq
    sudo rabbitmqctl add_user dev dev
    sudo rabbitmqctl set_permissions -p flask-rabbitmq dev ".*" ".*" ".*"
    sudo rabbitmqctl set_permissions -p / dev ".*" ".*" ".*"

    virtualenv -p /usr/bin/python3 env
    source env/bin/activate

    cd flask-rabbitmq
    pip install -r conf/python-requirements.txt
    sudo cp conf/supervisord.conf /etc/supervisor/
    sudo cp conf/supervisord.gunicorn.conf /etc/supervisor/conf.d/
    sudo cp conf/nginx.vhost.conf /etc/nginx/sites-available/default

    sudo /etc/init.d/supervisor restart
    sudo /etc/init.d/nginx restart


  SHELL
end
