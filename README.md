# email parser

This is a Python microservice that should extract data from input email as text

I will return JSON representation of the email as body text/plain, and headers like to, from email, from name, mail id, date processed

## Typical usecase
Postfix enabled on host linux server (Centos7), `/etc/aliases` file updated to redirect mail to a shell script that calls this microservice which can then decide where to pass the data downstream say to a ML/DL or NLP processor or some kind of database/datalake which can then further analysed

## steps to run
todo

### Locally with Pytest
todo

### Docker
todo

### Setting up the development environment
todo





## License

This application is licensed under the Apache License, Version 2. Separate third-party code objects invoked within this application are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache License FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)
