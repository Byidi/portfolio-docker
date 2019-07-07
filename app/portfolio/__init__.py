import os


from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import portfolio.utils.filters

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

    from portfolio.utils import filters
    app.register_blueprint(filters.blueprint)

    from portfolio import auth
    app.register_blueprint(auth.bp)

    from portfolio import blog
    app.register_blueprint(blog.bp)

    from portfolio import project
    app.register_blueprint(project.bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/contact/')
    def contact():
        return render_template('contact.html')

    @app.route('/apropos/')
    def apropos():
        return render_template('apropos.html')

    @app.route('/apropos/whoami/')
    def whoami():
        return render_template('whoami.html')

    @app.route('/apropos/cv/')
    def cv():
        return render_template('cv.html')

    return app
