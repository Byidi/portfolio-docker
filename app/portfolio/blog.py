from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from portfolio.auth import login_required
from portfolio.models.user import User
from portfolio.models.article import Article, Category

from portfolio.utils.tools import slugify

bp = Blueprint('blog', __name__, url_prefix='/blog')

@bp.route('/')
def index():
    articles = Article.query.filter(Article.publishedDate != -1).order_by(Article.publishedDate).all()
    return render_template('blog/list.html', articles=articles)

@bp.route('/article/<int:id>')
@bp.route('/article/<int:id>/<string:slug>')
def showArticle(id=None, slug=None):
    article = Article.query.filter(Article.id == id).first()
    return render_template('blog/show.html', article=article)

@bp.route('/category/<int:id>')
@bp.route('/category/<int:id>/<string:slug>')
def listArticleFromCategory(id=None, slug=None):
    articles = Article.query.filter(Article.publishedDate != -1).filter(Article.category_id == id)
    return render_template('blog/list.html', articles=articles)
