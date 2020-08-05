from flask import Flask
from flask_restplus import Api, Resource, fields
from emailParser import parse_email_parts as mail_parse

app = Flask(__name__)
api = Api(
    app,
    version="3.0.0",
    title="Email parser Service",
    description="This is a microservice that extracts email parts for the Breaking News Project",
)

emailNS = api.namespace(
    "Email",
    description="Operations associated with email parsing",
)


emailMesage = api.model(
    "emailMesage",
    {
        "emailText": fields.String(
            required=True, description="full raw email including headers and boundries"
        ),
    },
)

@emailNS.route("/parse")
@emailNS.response(404, "Invalid email")
class ParseEmail(Resource):
    @currencyNS.doc("parse_email_meta")
    @currencyNS.expect(emailMesage)
    @currencyNS.marshal_with(emailMesage, code=201)
    def post(self):
        if "emailText" in api.payload:
            return mail_parse(api.payload["emailText"])
        else:
            api.abort(400, "pass in email as raw text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8808)
