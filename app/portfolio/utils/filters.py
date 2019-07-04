import jinja2
import flask

blueprint = flask.Blueprint('filters', __name__)

@blueprint.app_template_filter()
def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    from datetime import datetime
    return datetime.utcfromtimestamp(value).strftime(format)

@blueprint.app_template_filter()
def folder(value):
    return value.split('.')[0]
    
@blueprint.app_template_filter()
def slug(str):
    import re
    slug = re.sub("[!@#$%^&*()[\]{};:,\\|./<>?|~=+]", "", str)
    slug = slug.replace(' ','_')
    return slug
