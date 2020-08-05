# email parser

This is a Python microservice that should extract data from input email as text

I will return JSON representation of the email as body text/plain, and headers like to, from email, from name, mail id, date processed

## typical usecase
Postfix enabled on host linux server (Centos7), `/etc/aliases` file updated to redirect mail to a shell script that calls this microservice which can then decide where to pass the data downstream say to a ML/DL or NLP processor or some kind of database/datalake which can then further analysed



