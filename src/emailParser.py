from email.parser import Parser as emp
from email.message import Message as emm
from src.errors.UserDefinedErrors import NoTextPartFound
import pdb

def parse_email(email_text):
    email_msg = emp().parsestr(email_text)
    return email_msg

def parse_email_parts(email_text):
    email_text_body = None
    email_msg = parse_email(email_text)

    #
    email_body_text = get_email_body_text(email_msg)

    return { 'body_text': email_body_text }

def get_email_body_text(email_msg):
    payloads = email_msg.get_payload()
    #usually text and html
    #
    for payload in payloads:
        #pdb.set_trace()
        if type(payload) is emm:
            if payload.get_content_type() == 'text/plain':
                return payload.get_payload()
       
    return None
    #raise NoTextPartFound("no text part found")
            