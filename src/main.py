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

# to escape email msg for JSON use:
# https://www.freeformatter.com/json-escape.html

emailMesage = api.model(
    "emailMesage",
    {
        "emailText": fields.String(
            required=True, description="full raw email including headers and boundries, escaped for JSON"
        ),
    },
)

@emailNS.route("/parse")
@emailNS.response(404, "Invalid email")
class ParseEmail(Resource):
    @emailNS.doc("parse_email_meta")
    @emailNS.expect(emailMesage)
    def post(self):
        #breakpoint()
        if "emailText" in api.payload:
            result = mail_parse(api.payload["emailText"])
            return result
        else:
            api.abort(400, "pass in email as raw text")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=7878)
