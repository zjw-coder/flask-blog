# 简介

基于 flask 的博客 demo

平时在使用 hexo 的静态博客，受次启发想开发一个博客

# 预览
![](https://gitee.com/jzhmcoo1/jzhmcoo1picrepo/raw/master/img/blogoverview.jpg)

# 安装

```bash
$ git clone https://github.com/jzhmcoo1/MyBlog.git
$ cd MyBlog
```

On MacOS:

```bash
# create a virtualenv and activate it
$ python3 -m venv venv
$ . venv/bin/activate
```

On Windows cmd:

```
$ py -3 -m venv venv
$ venv\Scripts\activate.bat
```



# 本地运行

```bash
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask init-db
$ flask run
```

Or on Windows cmd:

```bash
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask init-db
> flask run
```

 Open http://127.0.0.1:5000 in your browser.

# 项目结构

```text
.
├── __init__.py // 工厂函数文件
├── auth.py // 账号相关操作的代码
├── blog.py // 博客文章相关代码
├── config.py // 对文件路径进行配置
├── db.py // 数据库相关代码
├── schema.sql // 初始化数据库（建表）的代码
├── setup.py // 配置相关代码
├── static 
│   ├── blog.css
│   ├── images
│   │   ├── bg4.jpg
│   │   ├── default
│   │   │   ├── default.jpg
│   │   │   └── post.jpg
│   │   ├── footer-bg.png
│   │   └── upload
│   │       ├── avatars
│   │       └── postImages
│   ├── styles.css
│   └── theme // bootstrap模版
│       ├── css
│       │   ├── maps
│       │   │   └── style.css.map
│       │   └── style.css
│       ├── images
│       ├── js
│       │   └── script.js
│       ├── plugins
│       │   ├── bootstrap
│       │   ├── fonts
│       │   ├── jQuery
│       │   ├── shuffle
│       │   ├── slick
│       │   └── themify-icons
│       └── scss
└── templates // 母版文件夹
    ├── Homepage.html
    ├── auth
    │   ├── info.html
    │   ├── login.html
    │   ├── register.html
    │   └── update.html
    └── blog
        ├── create.html
        ├── detail.html
        ├── index.html
        └── update.html
```

# TODO：

- [x] 登录，注销，注册功能
- [x] 支持图片上传
- [x] 个人资料页
- [x] 支持 markdown 写作
- [x] valine评论引入
- [ ] 目录功能
- [ ] 上传 md 文件
- [ ] 更美观的个人资料页
- [ ] 更改 md 渲染主题
- [ ] More

# 参考文档与博客：

Flask开发
- [欢迎来到 Flask 的世界 — Flask 中文文档（ 1.1.1 ）](https://dormousehole.readthedocs.io/en/latest/index.html)
- [Template Designer Documentation — Jinja Documentation (2.11.x)](https://jinja.palletsprojects.com/en/2.11.x/templates/)
- [Blackyukun/quiet: 支持上传 markdown 文件生成 html 的 flask 静态博客](https://github.com/Blackyukun/quiet)
- [Sitemap — Python-Markdown 3.2.2 documentation](https://python-markdown.github.io/sitemap.html)
- [基于flask的静态博客 - 后端 - 掘金](https://juejin.im/entry/5a8d8776f265da4e8b2feac7)
- [用回valine评论系统,valine评论框样式美化 | 小鸡](https://me.idealli.com/post/2d5da13e.html)
- [快速开始 | Valine 一款快速、简洁且高效的无后端评论系统。](https://valine.js.org/quickstart.html)


