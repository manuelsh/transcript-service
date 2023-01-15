# Gunicorn Configuration File
# From https://www.vultr.com/docs/how-to-deploy-fastapi-applications-with-gunicorn-and-nginx-on-ubuntu-20-04/

from multiprocessing import cpu_count

# Socket Path
bind = ['0.0.0.0:8000']

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/home/ubuntu/code/transcript-service/access_logs'
errorlog =  '/home/ubuntu/code/transcript-service/error_logs'