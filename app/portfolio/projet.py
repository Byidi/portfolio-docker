from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from portfolio.auth import login_required
from portfolio.models.user import User
from portfolio.models.article import Article, Category

from portfolio.utils.tools import slugify

bp = Blueprint('projet', __name__, url_prefix='/projet')

@bp.route('/')
def index():
    projets = Projet.query.order_by(Projet.date).all()
    return render_template('projet/showProjet.html', projets=projets)
