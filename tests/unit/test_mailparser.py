from src.emailParser import parse_email
from src.emailParser import parse_email_text

mail_file = '/home/developer/neo-postfix-processor/tests/mockdata/mail.samp'

def read_file_off_disk(mock_mail_message):
	with open(mock_mail_message) as emailfile:
		data = emailfile.read()
	return data

def test_mockmail():
	data = read_file_off_disk(mail_file)
	
	assert len(data) == 1672 

def test_readmail():
	data = read_file_off_disk(mail_file)
	assert len(data) == 1672
	actual = parse_email(data)
	text_type = actual.get_payload()[0].get_content_type()
	html_type = actual.get_payload()[1].get_content_type()
	assert text_type == 'text/plain'
	assert html_type == 'text/html'
	text = actual.get_payload()[0].get_payload()
	assert len(text) == 501

def test_read_text_off_mail():
	data = read_file_off_disk(mail_file)
	assert len(data) == 1672
	actual = parse_email_text(data)
	assert len(actual) == 501
	#** Confirm your subscription to the NI mate newsletter
	assert actual[:54] == '** Confirm your subscription to the NI mate newsletter'