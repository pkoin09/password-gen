import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import secrets
import string
import pyqrcode
from reportlab.pdfgen import canvas
from getpass4 import getpass


class Mailer:
    @staticmethod
    def send_email(sender, sender_password, receiver, attachment):
        subject = "Password and QR Code"
        body = ""

        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = subject

        msg.attach(MIMEBase("application", "octet-stream"))
        with open(attachment, "rb") as file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={attachment}")
            msg.attach(part)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, sender_password)
            server.sendmail(sender, receiver, msg.as_string())


def main():
    # Ask user input for length of the password
    while True:
        try:
            length = int(input("Length of password?: "))

            # Generate password
            if length > 0:
                password = generate_password(length)
            else:
                print("Value cannot be less than zero")
                raise ValueError("Invalid input: -ve number")

            # checks / validates the name_prompt (qr file name)
            while True:
                try:
                    name_prompt = input("The default file name is 'password_qr, would you like to change it? (y/n): ")

                    if name_prompt.lower() == "y":
                        name = input("What would you like to name your file? ")
                        qr_file = generate_qr(password, name)
                    elif name_prompt.lower() == "n":
                        # !!! test more
                        name = "password_qr"
                        qr_file = generate_qr(password, name)
                    else:
                        raise ValueError

                    # save the QR code as a PDF (optional step?)
                    pdf_filename = save_as_pdf(qr_file, name)

                    # Show generated password on terminal
                    print("Generated password:", password)
                    print("QR code filename:", pdf_filename)

                    '''
                    Prompt user to send QR by mail.
                    For this to work, it would require sender to provide Gmail's app-specific password.
                    '''

                    send_email_prompt = input("Do you want to send the email? (y/n): ")
                    if send_email_prompt.lower() == "y":
                        sender = input("Enter your Gmail account: ")
                        sender_password = getpass("Enter your Gmail 'app-specific password: ")
                        receiver = input("Enter the recipient's email: ")

                        Mailer.send_email(sender, sender_password, receiver, pdf_filename)

                    break
                # inside while loop false value
                except ValueError:
                    ValueError
            break
        # outside while loop false value
        except ValueError:
            ValueError


def generate_password(n):
    char = string.ascii_letters + string.digits
    pwd = ''.join(secrets.choice(char) for _ in range(n))
    return pwd


def generate_qr(p, name):
    qr = pyqrcode.create(p)
    qr_code_filename = f"{name}.png"
    qr.png(qr_code_filename, scale=6)
    return qr_code_filename


def save_as_pdf(qr_file, name):
    pdf_filename = f"{name}.pdf"
    c = canvas.Canvas(pdf_filename)
    c.drawImage(qr_file, 100, 400, width=200, height=200)
    c.save()
    return pdf_filename


if __name__ == "__main__":
    main()