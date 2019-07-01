import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from portfolio.db import db_session
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    from portfolio import auth
    app.register_blueprint(auth.bp)

    from portfolio import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
