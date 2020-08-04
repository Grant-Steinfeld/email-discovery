from email.parser import Parser as emp
from email.message import Message as emm
from email import policy
import datetime

def parse_email(email_text):
    email_msg = emp(policy=policy.default).parsestr(email_text)
    return email_msg

def parse_email_parts(email_text):
    email_msg = parse_email(email_text)  #legacy parser
    email_body_part = email_msg.get_body(('related', 'plain'))
    email_body_text = email_body_part and email_body_part.get_content()
    
    if email_body_text is not None and email_body_text.strip().endswith('</html>'):
        email_body_text = None

    from_ = email_msg['from']

    result = { 
        'Body': email_body_text ,
        'subject': email_msg['subject'],
        'message-id': email_msg['Message-Id'],
        'from_name': from_.addresses[0].display_name,
        'from':  from_.addresses[0].addr_spec
    }

    #merge py 3.5 > ... 
    # z = x | y          
    # 3.9+ ONLY
    return {**result, **timestamp_dict()}



def timestamp_dict():
    date_ = datetime.datetime.now()
 
    return {
        'hour': date_.hour,
        'day': date_.day,
        'year': date_.year,
        'month': date_.month,
        'weekday': date_.weekday(),
        'hour': date_.hour,
        'minute': date_.minute,
        'day_of_year': date_.timetuple().tm_yday,
        'short_date': date_.ctime() 
        }