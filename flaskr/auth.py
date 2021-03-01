import functools
import os
import shutil
import time
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, send_from_directory
)
from werkzeug.security import check_password_hash, generate_password_hash
from config import AVATAR_PATH
from config import ALLOWED_IMAGE_EXTENSIONS
from config import DEFAULT_PATH
from flaskr.db import get_db
from werkzeug.utils import secure_filename

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        avatar_file = request.files['avatar']
        if avatar_file:
            avatar_path = upload_avatar(avatar_file)
        else:
            avatar_path = upload_avatar(None)
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
                'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password, avatar) VALUES (?, ?, ?)',
                (username, generate_password_hash(password), avatar_path)
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


# 检查用户 id 是否已经存储在 session 中,并从数据库中获取用户数据
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


# 注销
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


def get_info(id):
    db = get_db()
    user_info = db.execute(
        'SELECT u.id, username, nickname, address, description, avatar'
        ' FROM user u'
        ' WHERE u.id = ?',
        (id,)
    ).fetchone()
    return user_info


def get_recent_ten_posts(id):
    db = get_db()
    query = 'select id, author_id, created, title, summary, postImage from ' \
            'post where author_id = ? ORDER BY created DESC '
    params = (id,)
    ten_posts = db.execute(
        query, params
    ).fetchmany(10)
    return ten_posts


@bp.route('/<int:id>/info', methods=('GET', "POST"))
def info(id):
    user_info = get_info(id)
    print(user_info['avatar'])
    posts = get_recent_ten_posts(id)
    return render_template('auth/info.html', info=user_info, posts=posts)


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
def update(id):
    """
    更新个人信息
    :param id:
    :return:
    """
    info = get_info(id)

    if request.method == 'POST':
        nick = request.form['nickname']
        addr = request.form['address']
        desc = request.form['description']
        file = request.files['avatar']
        if file:
            new_path = upload_avatar(file, info['avatar'])
        else:
            new_path = info['avatar']
        db = get_db()
        db.execute(
            'UPDATE user SET nickname = ?, address = ?, description = ?, avatar = ?'
            'WHERE id = ?',
            (nick, addr, desc, new_path, id)
        )
        db.commit()
        # return render_template('auth/info.html', info=info)
        return redirect(url_for('auth.info', id=info['id']))
    return render_template('auth/update.html', info=info)


def allowed_file(filename):
    """
    检查文件的合法性
    :param filename:
    :return:
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGE_EXTENSIONS


def upload_avatar(get_file, old_file=""):
    file = get_file
    if file is not None:
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if not os.path.exists(AVATAR_PATH):  # 创建文件路径
            os.makedirs(AVATAR_PATH)
        if file and allowed_file(file.filename):
            filename = secure_filename(time.strftime("%Y%m%d%H%M%s") + "." + file.filename.rsplit('.', 1)[1].lower())
            file_path = os.path.join(AVATAR_PATH, filename)
            if old_file:  # 替换旧头像
                os.remove(os.path.join(AVATAR_PATH, old_file))
            # print(file_path)
            file.save(file_path)
            return filename
    new_name = secure_filename(time.strftime("%Y%m%d%H%M%s") + "." + "jpg")
    new_path = os.path.join(AVATAR_PATH, new_name)
    shutil.copy(DEFAULT_PATH, new_path)
    return new_name

