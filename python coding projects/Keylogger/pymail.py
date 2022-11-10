import smtplib

sender_email = "theronnie.rays@gmail.com"
rec_email = "tritans472@gmail.com"
password = input(str("enter the password:"))
message = "hey, this was sent using python"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("login success")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)