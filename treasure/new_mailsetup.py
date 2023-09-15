# from flask import Flask, jsonify, request
import smtplib  # Import smtplib for the actual sending function
from email.message import EmailMessage  # Import the email modules we'll need
from flask import Flask, request, url_for
import codecs
recipients = ['srikanth@xrmonk.com', 'saikrishna@themoe.com']

# themoe_gmail_app_password = 'tfhuqepamclgetua'
# themoe_gmail_id = 'support@themoe.com'

xrmonk_gmail_app_password = 'lzkrhqabzqleljmp'
xrmonk_gmail_id = 'support@xrmonk.com'


def email_send(email, choice, otp_code):
    # email = request.form.get('email')
    # SMTP stuff
    print('sending mail to', email)
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    print('sending...')
    s.starttls()
    # s.login(themoe_gmail_id, themoe_gmail_app_password)
    s.login(xrmonk_gmail_id, xrmonk_gmail_app_password)
    print('sending...after login....')

    # Email Notifications for each actions
    msg = EmailMessage()

    if choice == 4:
        msg['Subject'] = 'Qualifed student details'

        msg.set_content(
            f'This {email} has registered for treasure hunt sucessfully.')
    else:
        print(f'Please enter correct details')

    # the recipient's email address
    msg['From'] = 'TheMoe <support@themoe.com>'
    # msg['To'] = f'{email}'  # the sender's email address
    # for sending mail to  multiple recipients
    msg['To'] = ", ".join(recipients)
    s.send_message(msg)
    s.quit()
    return 'Email sent!'
