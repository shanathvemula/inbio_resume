from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

import email, smtplib, ssl
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# @csrf_exempt
def contact_form(request):
    data = dict(request.POST)
    print("contact", data)
    # emails = data['contact-email']
    # subject = data['subject'][0]
    # content = data['contact-message'][0]

    message = MIMEMultipart()
    message['From'] = 'sender@gmail.com'
    # message['cc'] = ccemails
    message['To'] = data['contact-email'][0]
    message['Subject'] = "Thank you for contacting me"
    with open('home/templates/thank_you.html', 'r') as file:
        body = file.read()
    body = body.replace('{{ fullname }}', data['contact-name'][0])
    message.attach(MIMEText(body, "html"))
    text = message.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(message['From'], 'password')
        print("login successfull")
        server.sendmail(data['contact-email'][0], data['contact-email'][0], text)
        print("Mail Sent Successfully")
        server.quit()

    return HttpResponse("OK")
