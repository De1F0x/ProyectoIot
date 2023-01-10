import os
from email.message import EmailMessage
import ssl 
import smtplib


class Email:

    def __init__(self):
        self.email = 'mikelandonimingo@gmail.com'
        self.contrasena ="mkhoascheqsldxhn"
        
    def send_email(self, rp, ass, cp):
        email_receptor = rp

        asunto = ass

        cuerpo = cp

        em = EmailMessage()

        em['From'] = self.email
        em['To'] = email_receptor
        em['Subject'] = asunto
        em.set_content(cuerpo)

        contexto = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = contexto) as smtp:
            smtp.login(self.email, self.contrasena)
            smtp.sendmail(self.email, email_receptor, em.as_string())
        
        