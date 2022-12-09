from store_app.models import Contact_us
from celery import shared_task
from django.core.mail import send_mail
from Magallanes import settings


@shared_task(bind=True)
def send_mail_func(self):
    users = Contact_us.objects.all()
    for i in range(1):
        mail_subject = "Hola! Testing Magallanes!"
        message = "Esto es un test enviado desde django"
        # Reemplazar por users.email
        to_email = "santiagocanovari+test@gmail.com"
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"
