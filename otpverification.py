from email.message import EmailMessage
import ssl
import random
import smtplib

OTP = random.randint(100000, 999999)

name = input("Enter your name: ")
receiver_email = input("Enter your email id: ")

def email_verification(receiver_email):
    email_check1 = ["gmail", "hotmail", "yahoo", "outlook"]
    email_check2 = [".com", ".in", ".org", ".edu", ".co.in"]
    count = 0

    for domain in email_check1:
        if domain in receiver_email:
            count += 1
    for site in email_check2:
        if site in receiver_email:
            count += 1

    if "@" not in receiver_email or count != 2:
        print("Invalid email id")
        new_receiver_email = input("Enter correct email id: ")
        return email_verification(new_receiver_email)
    return receiver_email

# Validate and set receiver_email
receiver_email = email_verification(receiver_email)

email_sender = "haranya135@gmail.com"
email_password = "nhyl ohcn dsyi zzyv"

subject = "OTP verification using python"
body = "Dear"+" "+name+","+"\n"+"\n"+"Your OTP is "+str(OTP)+"."

em = EmailMessage()
em['From'] = email_sender
em['To'] = receiver_email
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, receiver_email, em.as_string())

def sending_otp(receiver_email):
    new_otp = random.randint(100000, 999999)

    body = f"Dear {name},\n\nYour OTP is {new_otp}."
    subject = "OTP verification using python"
    message = f'subject:{subject}\n\n{body}'

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_sender, email_password)
        server.sendmail(email_sender, receiver_email, message)

    print("OTP has been sent to", receiver_email)
    received_OTP = int(input("Enter OTP: "))

    if received_OTP == new_otp:
        print("OTP verified")
    else:
        print("Invalid OTP")
        print("Resending OTP.....")
        sending_otp(receiver_email)

print("OTP has been sent to", receiver_email)
received_OTP = int(input("Enter OTP: "))

if received_OTP == OTP:
    print("OTP verified")
else:
    print("Invalid OTP")
    answer = input("Enter 'yes' to resend OTP on the same email and 'no' to enter a new email id: ")
    if answer.lower() == 'yes':
        sending_otp(receiver_email)
    elif answer.lower() == 'no':
        new_receiver_email = input("Enter new email id: ")
        email_verification(new_receiver_email)
        sending_otp(new_receiver_email)
    else:
        print("Invalid input")

    
