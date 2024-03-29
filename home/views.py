from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.mail import send_mail

from django.template.loader import render_to_string
from django.utils.html import strip_tags

import email, smtplib, ssl
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# @csrf_exempt
# def contact_form(request):
#     data = dict(request.POST)
#     print("contact", data)
#     emails = data['contact-email']
#     subject = data['subject'][0]
#     content = data['contact-message'][0]
#
#     html_message = render_to_string('thank_you.html', {'fullname': data['contact-name'][0]})
#     # print(html_message)
#     plain_message = strip_tags(html_message)
#     # print(plain_message)
#     send_mail(subject=subject, message=plain_message.lstrip(), from_email='sender@outlook.com',
#               recipient_list=emails)
#     return HttpResponse("OK")

# @csrf_exempt
# def contact_form(request):
#     data = dict(request.POST)
#     print("contact", data)
#     # emails = data['contact-email']
#     # subject = data['subject'][0]
#     # content = data['contact-message'][0]
#
#     ############################## creating message for the thank you mail ##############################
#     message = MIMEMultipart()
#     message['From'] = 'shanath1213@gmail.com'
#     # message['cc'] = ccemails
#     message['To'] = data['contact-email'][0]
#     message['Subject'] = "Thank you for contacting me"
#     with open('home/templates/thank_you.html', 'r') as file:
#         thank_you_body = file.read()
#         file.close()
#     thank_you_body = thank_you_body.replace('{{ fullname }}', data['contact-name'][0])
#     message.attach(MIMEText(thank_you_body, "html"))
#     thank_you_text = message.as_string()
#
#     ############################## creating message for sending contact text to mail ##############################
#     message2 = MIMEMultipart()
#     message2['From'] = 'shanath1213@gmail.com'
#     message2['To'] = 'shanathvemula@gmail.com'
#     message2['Subject'] = "Contact From is submitted from Portfolio"
#     with open('home/templates/contact_from_protfolio.html', 'r') as contact_file:
#         contact_body = contact_file.read()
#         contact_file.close()
#     contact_body = contact_body.replace('{{ contact-name }}', data['contact-name'][0]).replace('{{ contact-phone }}',
#                                                                                                data['contact-phone'][
#                                                                                                    0]).replace(
#         '{{ contact-email }}', data['contact-email'][0]).replace('{{ subject }}', data['subject'][0]).replace(
#         '{{ contact-message }}', data['contact-message'][0])
#     message2.attach(MIMEText(contact_body, "html"))
#     contact_text = message2.as_string()
#
#     ############################## Sending mails ##############################
#     context = ssl.create_default_context()
#     with smtplib.SMTP("smtp.gmail.com", 465) as server:
#         server.ehlo()
#         server.starttls()
#         server.ehlo()
#         server.login(message['From'], 'rnue kwjg teci nmeo')
#         print("login successfull")
#         server.sendmail(data['contact-email'][0], data['contact-email'][0], thank_you_text)
#         server.sendmail(message2['From'], message2['To'], contact_text)
#         print("Mail Sent Successfully")
#         server.quit()
#
#     return HttpResponse("OK")

import yagmail


@csrf_exempt
def contact_form(request):
    data = dict(request.POST)
    print("contact", data)
    from_mail = "sender@gmail.com"
    app_password = "gmail app password"

    ############################## creating message for the thank you mail ##############################
    to_1 = data['contact-email'][0]
    subject_1 = "Contact From is submitted from Portfolio"
    with open('home/templates/thank_you.html', 'r') as file:
        thank_you_body = file.read()
        file.close()
    thank_you_body = thank_you_body.replace('{{ fullname }}', data['contact-name'][0])

    ############################## creating message for sending contact text to mail ##############################
    to_2 = 'contact_recevier@gmail.com'
    subject_2 = "Contact From is submitted from Portfolio"
    with open('home/templates/contact_from_protfolio.html', 'r') as contact_file:
        contact_body = contact_file.read()
        contact_file.close()
        contact_body = contact_body.replace('{{ contact-name }}', data['contact-name'][0]).replace(
            '{{ contact-phone }}',
            data['contact-phone'][
                0]).replace(
            '{{ contact-email }}', data['contact-email'][0]).replace('{{ subject }}', data['subject'][0]).replace(
            '{{ contact-message }}', data['contact-message'][0])

    ############################## Sending mails ##############################
    with yagmail.SMTP(from_mail, app_password, 'smtp.gmail.com', 465) as yag:
        yag.send(to_1, subject_1, thank_you_body)
        yag.send(to_2, subject_2, contact_body)
        print('Sent email successfully')
        yag.close()
    return HttpResponse("ok")
