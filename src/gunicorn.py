from multiprocessing import cpu_count

_home_dir = "/home/vagrant/flask-rabbitmq/src"
user = "ubuntu"
group = "ubuntu"
reload = True
chdir = _home_dir
bind = "127.0.0.1:8000"
workers = (cpu_count() * 2) + 1
accesslog = "%s/logs/gunicorn-access.log" % _home_dir
errorlog =  "%s/logs/gunicorn-error.log" % _home_dir
timeout = 180
