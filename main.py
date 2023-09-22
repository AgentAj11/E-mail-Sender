import smtplib # to access SMTP
import ssl # for secure mail exchange
import credentials as cd # sender's credentials
# To add attachments into the mail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mailer(object):
    def __init__(self):
        self.smtp_server = "smtp.gmail.com" # define the server from which mail will be sent (here G-mail)
        self.smtp_port = 587 # Standard smtp port
        self.context = ssl.create_default_context()
        self.recipients = ["tomarg902@gmail.com", "devJujutsu@gmail.com", "GAURAVTOMAR.CSE.20021086@gehu.ac.in"]
        self.sender = cd.user
        self.senders_pwd = cd.pwd
        self.plain_body = ""
        self.html_body = ""
        self.server = None # server object

    def create_body(self):
        self.plain_body = """
        Hello, this is Agent AJ11.
        You have been observed right candidate for our upcoming mission.
        Reporting--> Dehradun ISBT at 18th Hr, man in dhoti kurta.
        """

        self.html_body = """
        <html>
            <body>
                <p>
                    Hello, this is Agent AJ11.<br>
                    <b>You have been observed right candidate for our upcoming mission.<b>
                    Reporting--> <u>Dehradun ISBT, man in dhoti kurta.</u><br>
                </p>
            </body>
        </html>
        """

    def transport(self):
        try:
            print("Connecting to the Gmail server...")
            self.server = smtplib.SMTP(self.smtp_server, self.smtp_port) # Establish the connection
            self.server.starttls(context=self.context)  # Make the connection secure by TLS
            self.server.login(self.sender, self.senders_pwd) # Login to G-mail
            print("Connected!")
            print()
            # Sending mails individually
            for person in self.recipients:
                print(f"Sending mail to {person}")

                Mail = MIMEMultipart()
                Mail['From'] = cd.user
                Mail['To'] = person
                Mail['Subject'] = "Bootcamp declaration"
                # Mail.attach(MIMEText(self.plain_body, "text"))
                Mail.attach(MIMEText(self.html_body, "html"))

                self.server.sendmail(self.sender, person, Mail.as_string())
                print(f"Mail successfully sent to {person}")

        except Exception as e:
            print("Failed.")
            print(e)
        finally:
            self.server.quit()


def main():
    post_master = Mailer()
    post_master.create_body()
    post_master.transport()

main()
