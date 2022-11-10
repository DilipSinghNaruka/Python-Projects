
#in this dont show your identy 

# import smtplib    
# sender_mail = "idf819425@gmail.com"   
# receivers_mail = "tritans472@gmail.com"
# password = input("enter your password ")   
# message = """From: From Person  
# To: To Person   
# Subject: Sending SMTP e-mail   
# This is a test e-mail message.  
# """  

# server = smtplib.SMTP('smtp.gmail.com',587) 
# server.ehlo()
# server.starttls()
# server.login(sender_mail,password)
# print("login succesfull")
# server.sendmail(sender_mail,receivers_mail,message)
# print("email has been send",receivers_mail)







#in this show your identy 


import smtplib    
sender_mail = input("type sender email :-")   
receivers_mail = input("type receiver email :-")
password = input("enter sendrer  password ")   
message = input("type message :-")

server = smtplib.SMTP('smtp.gmail.com',587) 
server.ehlo()
server.starttls()
server.login(sender_mail,password)
print("login succesfull")
server.sendmail(sender_mail,receivers_mail,message)
print("email has been send",receivers_mail)