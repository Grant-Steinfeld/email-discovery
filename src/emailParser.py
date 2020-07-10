from email.parser import Parser as emp
from src.errors.UserDefinedErrors import NoTextPartFound

def parse_email(email_text):
    email_msg = emp().parsestr(email_text)
    return email_msg

def parse_email_text(email_text):
    email_text_body = None
    email_msg = parse_email(email_text)
    #find text portion

    payloads = email_msg.get_payload()
    for payload in payloads:
        if payload.get_content_type() == 'text/plain':
            return payload.get_payload()
        else:
            raise NoTextPartFound("no text part found")
            