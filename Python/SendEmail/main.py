import smtplib
# from email.mime.text import MIMEText

EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.office365.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "moocs@iihmr.edu.in"
EMAIL_HOST_PASSWORD = "!ihmr@2017"
DEFAULT_FROM_EMAIL = 'moocs@iihmr.edu.in'

SEND_MAIL_TO = 'bhumik@drcsystems.com'


if EMAIL_USE_TLS:
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.set_debuglevel(1)
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

text_subtype = 'plain'
content = """
        Hello,
            This is a testing email."""
subject = "Testing Email"
subject = "Testing Email"

# msg = MIMEText(content, text_subtype)
# msg['Subject'] = subject
# msg['From'] = DEFAULT_FROM_EMAIL

server.sendmail(DEFAULT_FROM_EMAIL, SEND_MAIL_TO, content)
server.quit()
