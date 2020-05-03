from flask import Flask, request
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask_restplus import Api, Resource

# source: https://preslav.me/2018/12/02/designing-well-structured-rest-apis-with-flask-restplus-part-1/

app = Flask(__name__)
api = Api(app=app)
ns_conf = api.namespace('conferences', description='Conference operations')
ns_other = api.namespace('other')

@ns_other.route("/other")
@ns_conf.route("/conferences/")
class ConferenceList(Resource):
    def get(self):
        req = request.path.split("/")[1]
        """
        returns a list of conferences
        """

    def post(self):
        """
        Adds a new conference to the list
        """


@ns_conf.route("/conferences/<int:id>")
class Conference(Resource):
    def get(self, id):
        """
        Displays a conference's details
        """

    def put(self, id):
        """
        Edits a selected conference
        """ 

if __name__ == '__main__':
    app.run(debug=True)