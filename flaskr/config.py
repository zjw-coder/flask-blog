#!/usr/bin/env python
# encoding: utf-8
"""
:author: lixing
:file: config.py.py
:time: 2020/5/17 20:46
:file_desc: 
"""
import os

SECRET_KEY = b'Kg\x93(p\xc8\x84\xdbk\xc9\x8e\x8f\x04\xf3(\xf3'

# AVATAR_PATH = './static/images/upload/avatars'

ALLOWED_IMAGE_EXTENSIONS = {'jpg', 'png', 'jpeg'}

AVATAR_PATH = os.path.join(os.path.dirname(__file__), 'static/images/upload/avatars')
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'static/images/default/default.jpg')
POST_PATH = os.path.join(os.path.dirname(__file__), 'static/images/upload/postImages')
DEFAULT_POST_PATH = os.path.join(os.path.dirname(__file__), 'static/images/default/post.jpg')
