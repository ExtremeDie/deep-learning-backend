from flask_restplus import Resource
from flask import Flask
from apis import api
import os

app = Flask(__name__)
api.init_app(app)


@api.route('/status')
class status(Resource):
    def get(self):
        return {
            'status': True,
            'message': "Welcome to " + api.title,
            'version': api.version,
            'currentPath': os.getcwd()
        }


if __name__ == "__main__":
    # app.run(host='127.0.0.1', debug=True) # port 5000
    app.run(host='0.0.0.0') # port 5000