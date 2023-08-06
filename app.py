# This project has been created by Shreeharan for the YouTube Channel Stark Intelligence
import smtplib, ssl

# inputs
sender_email = input("Enter your email address and press enter: ")
password = input("Enter your password and press enter: ")
receiver_email = input("Enter the receiver email address and press enter: ")
input_message = input("Enter the message and press enter: ")

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = sender_email
receiver_email = receiver_email
message = input_message

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    
    if sender_email and password and receiver_email and input_message != None:


       server.login(sender_email, password)
       server.sendmail(sender_email,             receiver_email, message)

       print("Message sent successfully!")
    else:
       print("An error occured! Please try again later!")
