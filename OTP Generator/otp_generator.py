import secrets, string, time, smtplib
from email.message import EmailMessage

OTP_Length = 6
OTP_Expiry_Seconds = 120

Email_Sender = "example@gmail.com"
Email_Password = "example123"
SMTP_Server = "smtp.gmail.com"
SMTP_Port = 587

def generate_otp(length=OTP_Length):
    digits = string.digits
    return ''.join(secrets.choice(digits) for _ in range(length))

def send_otp_email(receiver_email, otp):
    msg = EmailMessage()
    msg["Subject"] = "Your OTP Code"
    msg["From"] = Email_Sender
    msg["To"] = receiver_email
    msg.set_content(f"Your OTP is: {otp}\nValid for 2 minutes.")

    with smtplib.SMTP(SMTP_Server, SMTP_Port) as server:
        server.starttls()
        server.login(Email_Sender, Email_Password)
        server.send_message(msg)

def send_otp_sms(phone_number, otp):
    print(f"[SMS SENT to {phone_number}] OTP: {otp}")

def main():
    print("OTP Verification System")
    print("------------------------")

    method = input("Choose delivery method (email/sms): ").strip().lower()

    otp = generate_otp()
    otp_created_time = time.time()

    if method == "email":
        email = input("Enter your email: ")
        send_otp_email(email, otp)
        print("OTP sent to email.")
    elif method == "sms":
        phone = input("Enter your phone number: ")
        send_otp_sms(phone, otp)
    else:
        print("Invalid method.")
        return

    user_otp = input("Enter OTP: ")

    if time.time() - otp_created_time > OTP_Expiry_Seconds:
        print("❌ OTP expired.")
    elif user_otp == otp:
        print("✅ OTP verified successfully!")
    else:
        print("❌ Invalid OTP.")

if __name__ == "__main__":
    main()