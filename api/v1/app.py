#!/usr/bin/python3
"""
module that runs the Flask app
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
'''from os import getenv
from flask_cors import CORS'''

app = Flask(__name__)
'''cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})'''
app.register_blueprint(app_views)

'''
@app.errorhandler(404)
def page_not_found(exceptions):
    """error handler function"""
    return jsonify(error="Not found"), 404

'''


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host=getenv('HBNB_API_HOST'), port=getenv('HBNB_API_PORT'),
            threaded=True)
