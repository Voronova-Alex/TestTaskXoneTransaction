import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expense_manager.settings')

app = Celery('expense_manager')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    # Executes every day morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'user_app.tasks.send_morning_email',
        'schedule': crontab(minute=30, hour=7)
    },
}
