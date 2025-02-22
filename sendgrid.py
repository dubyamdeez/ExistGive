from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = "your_sendgrid_api_key"

def send_email(donor_email, subject, content):
    message = Mail(
        from_email="your_email@yourorganization.org",
        to_emails=donor_email,
        subject=subject,
        plain_text_content=content
    )

    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    return response.status_code
