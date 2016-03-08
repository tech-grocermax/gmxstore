"""
Application configuration entry point and helper routines.

The configuration entry point supports debug and testing
options. Helpers also exist to load configuration data from
a configuration object or via an environment variable.
"""
from logging import basicConfig, getLogger, DEBUG
from logging.config import dictConfig

from flask import request

from gmxstore import defaults
from gmxstore.controllers import create_routes


def configure_app(app, debug=False, testing=False):
    """
    Configure the application.

    Allows the application to be configured for interactive debugging or unit testing.

    If debug is enabled, `app.run()` will reload on source changes (assuming application
    code is installed in "editable" mode). If testing is enabled, the collaborators
    defined below may be modified to use mocks. Both settings change how uncaught
    exceptions are handled, either by logging to the console (debug) or propagating to the
    test client (testing).
    """

    app.debug = debug
    app.testing = testing

    _configure_from_defaults(app)
    _configure_from_environment(app)
    _configure_stream_reading(app)
    _configure_logging(app)

    # Configure other collaborators (or mocks) here

    # Hook up controllers
    create_routes(app)


def _configure_from_defaults(app):
    """
    Load configuration defaults from defaults.py in this package.
    """
    app.config.from_object(defaults)


def _configure_from_environment(app):
    """
    Load configuration from a file specified as the value of
    the GMXSTORE_SETTINGS environment variable.

    Don't complain if the variable is unset.
    """
    app.config.from_envvar("GMXSTORE_SETTINGS", silent=True)


def _configure_stream_reading(app):
    """
    Ensure that nginx and uwsgi place nicely together.

    Under some error conditions, uwsgi will simply close its socket, causing clients
    to hang waiting for a response. See NS-281.
    """
    if app.config.get('FORCE_READ_REQUESTS'):
        @app.after_request
        def read_request(response):
            request.stream.read()
            return response


def _configure_logging(app):
    """
    Configure logging using timber.
    """
    if app.testing or app.debug:
        basicConfig(level=DEBUG)
    else:
        dictConfig(app.config.get("LOGGING"))
        configured_logger = getLogger("gmxstore")

        # ensure that Flask's logger uses configured handlers
        for handler in configured_logger.handlers:
            app.logger.addHandler(handler)

        app.logger.debug("Initialized logging")
