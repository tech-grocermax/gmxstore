"""
filters.py

Version-agnostic decorators that can be applied to controller functions
"""
from functools import wraps
from flask import abort, request, url_for, current_app as app
from requests import codes

#from receiptservice.database_operations import get_credential_id, get_admin
from gmxstore.errors import BadInputParam

def extract_apk_detail(fname):
    """
    used to extract apk details from the apk file name
    args:
    fname: apk file name
    """
    apkname = fname.split('-', 2)[0]
    version = fname.split('-', 2)[1].replace('.apk','')
#    return {"id": app.config['PACKAGE_DETAILS'][apkname]["id"], "name": app.config['PACKAGE_DETAILS'][apkname]["name"], 
 #       "version": version, "package": apkname, "version_code": app.config['PACKAGE_DETAILS'][apkname]["version_code"],
  #      "app_url": request.url_root + url_for('static', filename='apk/'+fname), "icon_url": request.url_root+url_for('static', filename=app.config['PACKAGE_DETAILS'][apkname]["icon"])}
    return {"id": app.config['PACKAGE_DETAILS'][apkname]["id"], "name": app.config['PACKAGE_DETAILS'][apkname]["name"], 
        "version": version, "package": app.config['PACKAGE_DETAILS'][apkname]["package"], "version_code": app.config['PACKAGE_DETAILS'][apkname]["version_code"],
        "app_url": request.url_root + 'static/apk/' + fname, "icon_url": request.url_root+'static/'+app.config['PACKAGE_DETAILS'][apkname]["icon"]}


def auth_required(credentials):

    def decorator(f):
        @wraps(f)
        def decorated(*fargs, **fkwargs):
            if request.authorization != credentials:
                abort(codes.UNAUTHORIZED)
            return f(*fargs, **fkwargs)
        return decorated

    return decorator


def auth_user_credentials(f):
        @wraps(f)
        def decorated(*fargs, **fkwargs):
            if request.authorization and get_credential_id(request.authorization.get('username'),
                                                           request.authorization.get('password')):
                return f(*fargs, **fkwargs)
            abort(codes.UNAUTHORIZED)
        return decorated


def auth_admin(f):
        @wraps(f)
        def decorated(*fargs, **fkwargs):
            if request.authorization and get_admin(request.authorization.get('username'),
                                                   request.authorization.get('password')):
                return f(*fargs, **fkwargs)
            abort(codes.UNAUTHORIZED)
        return decorated


def expect_key(args, key):
    """
    A helper function to extract value of provided key
    """
    value = args.get(key)
    if not value:
        app.logger.info('{} parameter is missing.'.format(key))
        raise BadInputParam(key)

    return value
