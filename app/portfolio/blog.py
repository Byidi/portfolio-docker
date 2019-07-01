from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from portfolio.auth import login_required
from portfolio.models.user import User
from portfolio.models.article import Article, Category, Article_category

from portfolio.utils import slugify

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    articles = Article.query.filter_by(published=1).order_by(Article.publishDate).all()
    return render_template('blog/index.html', articles=articles)

@bp.route('/article/<int:id>')
@bp.route('/article/<int:id>/<string:slug>')
def showArticle(id=None, slug=None):
    article = Article.query.filter_by(id=id, published=1).first()
    return render_template('blog/article.html', article=article, test=test)
