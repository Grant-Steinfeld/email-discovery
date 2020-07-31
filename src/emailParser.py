from email.parser import Parser as emp
from email.message import Message as emm
from email import policy
from src.errors.UserDefinedErrors import NoTextPartFound, EmptyEmail

def parse_email(email_text):
    email_msg = emp(policy=policy.default).parsestr(email_text)
    return email_msg

def parse_email_parts(email_text):
    email_msg = parse_email(email_text)  #legacy parser
    
    email_body_part = email_msg.get_body(('related', 'plain'))
    email_body_text = email_body_part and email_body_part.get_content()
    from_ = email_msg['from']

    return { 
        'body_text': email_body_text ,
        'subject': email_msg['subject'],
        'message-id': email_msg['Message-Id'],
        
        'from_name': from_.addresses[0].display_name,
        'from':  from_.addresses[0].addr_spec
    }



