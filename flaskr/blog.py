import shutil

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.auth import login_required, allowed_file
from flaskr.db import get_db
from markdown import Markdown
from config import POST_PATH
from config import DEFAULT_POST_PATH
from werkzeug.utils import secure_filename
import time
import os

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, summary, body, created, author_id, username, postImage'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        summary = request.form['summary']
        body = request.form['body']
        postImage = request.files['postImage']
        if postImage:
            post_path = upload_postImage(postImage)
        else:
            post_path = upload_postImage(None)
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, summary, body, author_id, postImage)'
                ' VALUES (?, ?, ?, ?,?)',
                (title, summary, body, g.user['id'], post_path)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, summary, body, created, author_id, username, postImage'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    # if check_author and post['author_id'] != g.user['id']:
    #     abort(403)

    return post


@bp.route('/<int:id>')
def get_post_in_detail(id):
    post = get_post(id)
    post_body = markdown_to_html(post)
    return render_template('blog/detail.html', post=post, post_body=post_body)


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        summary = request.form['summary']
        body = request.form['body']
        post_file = request.files['postImage']
        if post_file:
            new_path = upload_postImage(post_file, post['postImage'])
        else:
            new_path = post['postImage']
        error = None

        if not title:
            error = 'Title is required.'
        if not body:
            error += 'Article is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?,summary = ?, body = ?, postImage = ?'
                ' WHERE id = ?',
                (title, summary, body, new_path, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))


def markdown_to_html(post):
    extension = ['fenced_code', 'codehilite',
                 'tables', 'sane_lists']
    md = Markdown(extensions=extension)
    post_html = md.convert(post['body'])
    return post_html


def upload_postImage(get_file, old_file=""):
    file = get_file
    if file is not None:
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if not os.path.exists(POST_PATH):  # 创建文件路径
            os.makedirs(POST_PATH)
        if file and allowed_file(file.filename):
            filename = secure_filename(time.strftime("%Y%m%d%H%M%s") + "." + file.filename.rsplit('.', 1)[1].lower())
            file_path = os.path.join(POST_PATH, filename)
            if old_file:  # 替换旧头像
                os.remove(os.path.join(POST_PATH, old_file))
            # print(file_path)
            file.save(file_path)
            return filename
    new_name = secure_filename(time.strftime("%Y%m%d%H%M%s") + "." + "jpg")
    new_path = os.path.join(POST_PATH, new_name)
    shutil.copy(DEFAULT_POST_PATH, new_path)
    return new_name
