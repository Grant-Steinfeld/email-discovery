from email.parser import Parser as emp
from email.message import Message as emm
from src.errors.UserDefinedErrors import NoTextPartFound, EmptyEmail

def parse_email(email_text):
    email_msg = emp().parsestr(email_text)
    return email_msg

def parse_email_parts(email_text):

    if (len(email_text.strip()) == 0):
        raise EmptyEmail("empty email")

    email_text_body = None
    email_msg = parse_email(email_text)

    email_body_text = get_email_body_text(email_msg)
    from_ = email_msg['from']

    return { 
        'body_text': email_body_text ,
        'subject': email_msg['subject'],
        'from_raw': from_,
        'from_name': get_email_address_name_utf8(from_),
        'from': get_just_email_address(from_)}

def get_email_body_text(email_msg):
    payloads = email_msg.get_payload()
    #usually text and html
    #
    for payload in payloads:
    
        if type(payload) is emm:
            if payload.get_content_type() == 'text/plain':
                return payload.get_payload()
       
    return None
    #raise NoTextPartFound("no text part found")

def get_just_email_address(address):
    
    plain_email = address
    first_angle_bracket = plain_email.find('<')
    if first_angle_bracket != -1:
        second_angle_bracket = plain_email.find('>')
        return plain_email[first_angle_bracket+1:second_angle_bracket]
    return plain_email

def get_email_address_name_utf8(address):
    address_name = ''
    #=?utf-8?Q?NI=20mate=20Newsletter?=
    utf8prefix = '=?utf-8?Q?'
    utf8suffix = '?='
    suffixIndex = address.find(utf8suffix)


    if address.startswith(utf8prefix):
        address_name = address[len(utf8prefix) : suffixIndex]
        #hack replace =20 (spaces)
        address_name = address_name.replace('=20',' ')
    return address_name
