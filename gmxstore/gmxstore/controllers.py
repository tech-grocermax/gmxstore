"""
Define controller mappings.

Uses a factory method to apply routes to the app.
It would also be possible to use blueprints.
"""
from os import listdir
from os.path import isfile, join

from flask import Response, jsonify
from requests import codes
from ujson import dumps

from filters import extract_apk_detail, authenticate_service_request

def create_routes(app):
    @app.route("/")
    def index():
        """
        Example: use value from application configuration as page content.
        """
        return app.config['MESSAGE']

    @app.route("/builds")
    @authenticate_service_request
    def get_builds():
        """
        Returns list of latest builds by reading builds from asset directory.
        """
        buildpath = app.config['APK_PATH']
        onlyfiles = [extract_apk_detail(f) for f in listdir(buildpath) if isfile(join(buildpath, f))]
        #return dumps({"result":onlyfiles}), codes.OKAY
#        return Response(response=jsonify(result=onlyfiles), status=codes.OKAY, mimetype=app.config['CONTENT_TYPE'])
        return jsonify(result=onlyfiles)
