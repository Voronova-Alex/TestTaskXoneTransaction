from expense_manager.celery import app

from .service import list_user_mail, send, user_info


@app.task
def send_morning_email():
    for i in list_user_mail():
        print(i)
        send(user_info(*i))
