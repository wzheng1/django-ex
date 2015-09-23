import os

os.environ['PRODUCTION'] = 'TRUE'
os.environ['DEMOSITE_DB_HOST'] = open('/var/www/demosite/etc/dbhost').read().strip()

def num_cpus():
    if not hasattr(os, "sysconf"):
        raise RuntimeError("No sysconf detected.")
    return os.sysconf("SC_NPROCESSORS_CONF")
    
bind = "127.0.0.1:8080"
workers = num_cups() * 2
max_requests = 1000
reload = True
