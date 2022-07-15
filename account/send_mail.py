
import smtplib
import os

EMAIL_ADDRESS = os.environ.get('Email_Auto_Stock')

EMAIL_PASSWORD = os.environ.get('Password_Auto_Stock')

def sendNewUserEmail(email_address):
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
  
        subject = 'Successfull signup'

        body = 'New account created!'

        msg = f'Subject:{subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS,email_address,msg)


