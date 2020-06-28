import smtplib
from email.mime.text import MIMEText


def send_mail(customer,dealer,rating,comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '17244259111ee9'
    password = 'f91efbfc359386'
    message = "<h3>New Feedback Sumission</h3><ul><li>: {}</li><li>Dealer: {}</li><li>Rating: {}</li><li>comments: {}</li></ul>".format(customer,dealer,rating,comments)


    sender_email = "sanjeevgupta15599@gmail.com"
    receiver_email = "sanjeevgupta9364@gmail.com"

    msg = MIMEText(message,'html')
    msg['Subject'] = "Lexus Feedback"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(smtp_server,port) as server:
        server.login(login,password)
        server.sendmail(sender_email,receiver_email,msg.as_string())