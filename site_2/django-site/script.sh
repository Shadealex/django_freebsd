#!/usr/local/bin/bash
NAME="site_2"                                             # Django Project Name
DJANGODIR=/var/www/site_2/django-site                        # Django Project Directory
SOCKFILE=/var/www/site_2/django-site/run/gunicorn.sock     # Gunicorn Sock File
USER=a.maslak                                                # Django Project Running under user vagrant
GROUP=a.maslak                                                # Django Project Running under group vagrant
NUM_WORKERS=3
PORT=8001
DJANGO_SETTINGS_MODULE=test_site.settings                     # change 'myproject' with your project name
DJANGO_WSGI_MODULE=test_site.wsgi                             # change 'myproject' with your project name
LOGFILE=/var/log/gunicorn/test_site_2.log
LOGDIR=$(dirname $LOGFILE)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source ../venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user=$USER --group=$GROUP \
    --bind=unix:$SOCKFILE \
    --log-level=debug \
    --log-file=$LOGFILE 2>>$LOGFILE \
    --bind 127.0.0.1:$PORT
