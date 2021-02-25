import os
import glob
from src.emailParser import parse_email
from src.emailParser import parse_email_parts

#home_dir = '/home/developer/neo-postfix-processor'
home_dir = os.path.dirname(os.path.realpath(__file__))
breakpoint()
mock_dir = home_dir + '/../mockdata'
out_dir = home_dir + '/output'
mail_file = mock_dir + '/mail.samp'
med_sample_dir = mock_dir + '/med-samp-mail'

def read_file_off_disk(mail_sample_path):
	with open(mail_sample_path) as emailfile:
		data = emailfile.read()
	return data

def get_list_files(dirpath, pattern='*.txt'):
	if dirpath.endswith( os.path.sep) == False:
		dirpath += os.path.sep
	return glob.glob("{}{}".format(dirpath, pattern))

def test_mockmail():
	data = read_file_off_disk(mail_file)
	
	assert len(data) == 1672 



def test_read_text_off_1_mail_file():
	data = read_file_off_disk(mail_file)
	assert len(data) == 1672
	actual = parse_email_parts(data)
	assert len(actual['Body']) == 501
	assert len(actual['subject']) == 47
	assert len(actual['message-id']) == 67
	assert 'day_of_year' in actual
	assert 'short_date' in actual

	assert actual['subject'] == 'NI mate Newsletter: Please Confirm Subscription'
	assert actual['Body'][:54] == '** Confirm your subscription to the NI mate newsletter'
	assert len(actual['from']) == 16
	assert len(actual['from_name']) == 18

	assert actual['message-id'] == '<9656357.20180313131359.5aa7ce976a5fb2.44907804@mail7.mcsignup.com>'
	assert actual['from'] == 'info@delicode.fi'
	assert actual['from_name'] == 'NI mate Newsletter'

def test_get_med_samp_mails():
	clean_output_body_dir(out_dir)
	mail_samples_list = get_list_files(med_sample_dir)
	assert len(mail_samples_list) == 33
	for i, mail_path in enumerate(mail_samples_list):
		email_text = read_file_off_disk(mail_path)
		if not email_text.strip():
			continue
		email_text_parts = parse_email_parts(email_text)

		assert type(email_text_parts) is dict	
		assert 'subject' in email_text_parts
		assert 'from' in email_text_parts
		assert 'Body' in email_text_parts
		assert 'day_of_year' in email_text_parts
		if email_text_parts.get('Body') is not None:
			write_file_text(i, email_text_parts['Body'])
			
		
		
	body_written_to_file_count = get_list_files(out_dir)
	assert len(body_written_to_file_count) == 27
	clean_output_body_dir(out_dir)
	body_written_to_file_count = get_list_files(out_dir)
	assert len(body_written_to_file_count) == 0
	



def write_file_text(id, data, path_=out_dir):
	path_ = f'{path_}/{id}_body.txt'
	with open(path_,'w') as nf:
		nf.write(data)


def test_get_mail_paths():
	actual = get_list_files(med_sample_dir)
	assert type(actual) is list
	assert len(actual) == 33


def clean_output_body_dir(path, ext='.txt'):
	filelist = [ f for f in os.listdir(path) if f.endswith(ext) ]
	for f in filelist:
		os.remove(os.path.join(path, f))