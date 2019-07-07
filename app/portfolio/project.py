from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from portfolio.auth import login_required
from portfolio.models.project import Project

from portfolio.utils.tools import slugify

bp = Blueprint('project', __name__, url_prefix='/project')

@bp.route('/')
def index():
    projects = Project.query.order_by(Project.date).all()
    return render_template('project/list.html', projects=projects)

@bp.route('/<int:id>')
@bp.route('/<int:id>/<string:slug>')
def show(id=None, slug=None):
    projects = Project.query.order_by(Project.date).all()
    project = Project.query.filter(Project.id == id).first()
    return render_template('project/show.html', project=project, projects=projects)
