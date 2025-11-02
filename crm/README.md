# CRM Celery & Redis Setup Guide

This document explains how to set up and run Celery with Redis and Celery Beat for scheduled CRM background tasks.

---

##  1. Install Redis and Dependencies

### For Ubuntu/Debian:
```bash
sudo apt update
sudo apt install redis-server

Verify Redis is running:

redis-cli ping

Expected output:

PONG

Install required Python packages:

Make sure your virtual environment is active, then install:

pip install celery redis django-celery-beat

Or install from requirements.txt:

pip install -r requirements.txt

 2. Run Database Migrations

Before starting Celery, run migrations to create the necessary Django tables (including django_celery_beat tables):

python manage.py migrate

 3. Start Celery Worker

Start the Celery worker that will process background tasks:

celery -A crm worker -l info

This will start listening for tasks sent to the Redis broker defined in your settings.py (e.g. redis://localhost:6379/0).
 4. Start Celery Beat

Start Celery Beat to schedule periodic tasks:

celery -A crm beat -l info

This will use the CELERY_BEAT_SCHEDULE defined in your crm/settings.py, for example:

CELERY_BEAT_SCHEDULE = {
    'generate-crm-report': {
        'task': 'crm.tasks.generate_crm_report',
        'schedule': crontab(day_of_week='mon', hour=6, minute=0),
    },
}

 5. Verify Logs

After both Celery Worker and Celery Beat are running, you can verify that tasks execute correctly.

Check the log file:

cat /tmp/crm_report_log.txt

Expected output format:

2025-11-02 06:00:00 - Report: 42 customers, 180 orders, $25,000 revenue

 6. Troubleshooting

    If you see ConnectionRefusedError, make sure Redis is running:

sudo systemctl status redis-server

If Celery tasks aren’t executing, check that both Celery Worker and Celery Beat are active and running in the correct virtual environment.

Ensure that your Django project settings include:

CELERY_BROKER_URL = 'redis://localhost:6379/0'