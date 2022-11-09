from expense_manager.celery import app
from .service import list_user_mail, user_info, send


@app.task
def send_moning_email():
    for i in list_user_mail():
        print(i)
        send(user_info(*i))
