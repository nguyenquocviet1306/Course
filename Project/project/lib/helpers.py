"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password
from webhelpers.html import escape, HTML, literal, url_escape
from webhelpers.html.tags import *
from pylons import url
from webhelpers.html.tags import link_to
from project.lib import auth
import hashlib
import urllib

def send_mail(SUBJECT, BODY,TO):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib
    gmail_name = 'nguyenquocviet1306@gmail.com'
    gmail_password = 'nguyenquocviet13061996'
    msg = MIMEMultipart()
    #msg['From'] = FROM
    msg['To'] = TO
    msg['Subject'] = SUBJECT
    HTML_BODY = MIMEText(BODY, 'html')
    msg.attach(HTML_BODY)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_name, gmail_password)
    server.sendmail(gmail_name, TO, msg.as_string())
    server.close()
    print ("sent")
