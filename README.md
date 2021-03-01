# 简介

基于 flask 的博客 demo

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



# 预览
![](https://gitee.com/jzhmcoo1/jzhmcoo1picrepo/raw/master/img/blogoverview.jpg)

# 安装

```bash
$ git clone https://github.com/jzhmcoo1/MyBlog.git
$ cd MyBlog
```

On Windows cmd:

```
$ py -3 -m venv venv
$ venv\Scripts\activate.bat
```



# 本地运行


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



