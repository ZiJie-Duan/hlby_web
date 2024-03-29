import os
from urllib.parse import unquote
from flask import Flask, render_template, session, redirect, url_for, flash,request, g
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required
from flask_login import logout_user, login_user
#这是一个黑利博瑞小型图文消息程序

#初始化登陆
login_manager = LoginManager()
#初始化路径
basedir = os.path.abspath(os.path.dirname(__file__))
#初始化app
app = Flask(__name__)
#初始化数据库设置
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#初始化登陆安全配置
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
app.config['SECRET_KEY']='qazxswqwedsazxc'
#初始化 
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)




#数据库---------模型声明----------

           #导入登陆模块
class Years(db.Model):
    #用于保存用户名以及密码的模型
    __tablename__ = 'years'
    #设置id表头
    id = db.Column(db.Integer, primary_key = True)
    year = db.Column(db.String(64), unique=True, index=True)
    describe = db.Column(db.Text)
    photo = db.Column(db.String(64))

    #外键被链接
    dets = db.relationship('Det', backref='role')

    #返回函数
    def __repr__(self):
        return "%r*!sqlite!*%r*!sqlite!*%r" % (self.year,self.describe,self.photo)


class Det(db.Model):
    #用于保存照片的模型
    __tablename__ = 'det'
    #设置id表头
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique=True, index=True)
    describe = db.Column(db.Text)
    photo = db.Column(db.String(64))
    body = db.Column(db.Text)

    #设定外键（有可能这个注释是错误的）
    year_id = db.Column(db.Integer, db.ForeignKey('years.id'))
    #返回函数
    def __repr__(self):
        return "%r*!sqlite!*%r*!sqlite!*%r*!sqlite!*%r" % (self.name,self.describe,self.photo,self.body)

#数据库---------模型声明----------





db.create_all()

#b = Years(year = "2019年上半学期",describe = "快乐的一学期",photo = "/static/img/year_min/a.jpg")
#d = Det(name = "丑陋的素颜学生们",describe = "快乐的军训",photo = "/static/img/det_min/a.jpg",body="h1ƒ这是一个大标题∂h6ƒ\"这是一个小标题\"",role=b)
#c = Act(activity = "第一次校会",hphoto="1.jpg",file_wjj = "a",describe="这是我们第一次校会哈哈哈哈哈")
#g = Act(activity = "第二次校会",hphoto="5.jpg",file_wjj = "b",describe="这是我们第er次校会哈哈哈哈哈")
#d = Potx(photoname = "2.jpg",describe="这也不知道是啥",role = c)
#e = Potx(photoname = "3.jpg",describe="这也不知道是啥",role = c)
#f = Potx(photoname = "4.jpg",describe="这也不知道是啥",role = c)
#db.session.add_all([a,b,c,d,e,f,g])
#db.session.add(b)
#db.session.add(d)

#db.session.commit()
