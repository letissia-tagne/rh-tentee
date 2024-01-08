import logging
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail


logger = logging.getLogger( __name__  )
def send_email_with_html_body(sujet: str, receivers: list, template:str, context: dict):
    """ this focntion help to send a customize email to a specific user or set of users """
    try:
         message=render_to_string(template, context)
         send_mail(
             subjet,
             message,
             settings.EMAIL_HOST_USER
             fail_silently= True
             html_message= mmessage
             
         )
         return True
         
    except Exception as e:
        logger.error(e)