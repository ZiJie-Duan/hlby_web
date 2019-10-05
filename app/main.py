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






#url映射 ------ ------- ------- ------- --------

#错误反馈
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#错误反馈
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500




#主页映射路由
@app.route('/')
def index():
    #获取数据库中所有年度信息
    a = Years.query.all()

#self.year,self.describe,self.photo
    z_list = []

    for x in a:
        #循环分割数据
        a = str(x)
        b = a.split("*!sqlite!*")
        wcl_list = []

        for y in b :
            c = y.strip('\'')

            wcl_list.append(c)

        z_list.append(wcl_list)

    return render_template('index.html',lista = z_list)



#活动选择路由
@app.route('/years/<v>/')
def year(v):
    #年度学期页面生成 self.year,self.describe,self.photo
    #self.activity,self.describe,self.photo
    #传入参数v进行year的查询，并查询关于活动具体图文的外链
    a = Years.query.filter_by(year=v).first()
    b = Det.query.filter_by(role=a).all()

    z_list = []

    for x in b:
        a = str(x)
        b = a.split("*!sqlite!*")
        wcl_list = []

        for y in b :
            c = y.strip('\'')

            wcl_list.append(c)

        z_list.append(wcl_list)


    return render_template('one.html',lista = z_list)



#具体图文路由
@app.route('/det/<v>/')
def det(v):
    #用于查询具体图文的函数 传入值v 进行活动的具体查询
    det_list = Det.query.filter_by(name=v).first()
    #活动选择 self.name,self.describe,self.photo,self.body)
    a = str(det_list)
    b = a.split("*!sqlite!*")
    wcl_list = []

    for y in b :

        c = y.strip('\'')

        wcl_list.append(c)

    z_list = []
    zw = wcl_list[-1]
    zw = zw.split("*!body!*")
    for x in zw:
        x = x.split("*!bodyson!*")
        z_list.append(x)


    return render_template('det.html',lista = z_list)




@app.route('/api/',methods=['POST'])
def apidk():
    #api post 提交方法
    
    #重点重点 ！！！中文post提交方法
    text = request.get_data()
    #重点重点 ！！！中文post提交方法

    if text is not None:

        #重点重点 ！！！中文post提交方法
        text = unquote(str(text), 'utf-8')
        #重点重点 ！！！中文post提交方法

        text = str(text)
        text = text[2:]
        text = text[:-1]


        a = str(text)
        d = a.strip("\"")
        zlist = d.split("*!http!*")


        if zlist[0] == "update":
            #模式为更新上传模式
            if zlist[1] == "year":
                #cho选择器为year
                tjb = Years(year = zlist[2],describe = zlist[3],photo = zlist[4])
                db.session.add(tjb)
                db.session.commit()
                return "ok"


            if zlist[1] == "det":
                #cho选择器为det
                print(zlist)
                a = Years.query.filter_by(year=zlist[6]).first()
                tjb = Det(name = zlist[2],describe = zlist[3],photo = zlist[4],body=zlist[5],role=a)
                db.session.add(tjb)
                db.session.commit()
                return "ok"



        if zlist[0] == "delete":
            #模式为删除模式
            if zlist[1] == "year":
                #cho选择器为year
                a = Years.query.filter_by(name=zlist[2]).first()
                db.session.delete(a)
                db.session.commit()
                return "ok"


            if zlist[1] == "det":
                #cho选择器为det
                a = Det.query.filter_by(name=zlist[2]).first()
                db.session.delete(a)
                db.session.commit()
                return "ok"



        if zlist[0] == "search":
            #模式为搜索模式

            if zlist[1] == "year":
                #cho选择器为year

                a = Years.query.all()

                return two_list_chuli(a)


            if zlist[1] == "det":
                #cho选择器为det

                a = Det.query.all()

                return two_list_chuli(a)



#用于上传图片的路由
@app.route("/api/upload/",methods=['POST'])
def upjpg():

    upload_file = request.files['file']
    
    old_file_name = upload_file.filename
    yz_name = old_file_name.split("*!*")
    print(old_file_name)
    print(yz_name)

    if upload_file:

        if yz_name[0] == "year":
            #file_path = os.path.join("hlby_web/static/img/year_min/", old_file_name)
            file_path = os.path.join("/Users/lucy/Desktop/hlby_web/app/static/img/year", old_file_name)

            upload_file.save(file_path)

        if yz_name[0] == "detm":
            #file_path = os.path.join("hlby_web/static/img/det_min/", old_file_name)
            file_path = os.path.join("/Users/lucy/Desktop/hlby_web/app/static/img/detm/", old_file_name)

            upload_file.save(file_path)

        if yz_name[0] == "det":
            #file_path = os.path.join("hlby_web/static/img/det/", old_file_name)
            file_path = os.path.join("/Users/lucy/Desktop/hlby_web/app/static/img/det/", old_file_name)

            upload_file.save(file_path)
        
        return '发送完成'
    else:
        return '发送失败'


def two_list_chuli(a):

    z_list = []

    for x in a:
        a = str(x)
        b = a.split("*!sqlite!*")
        wcl_list = []

        for y in b :
            c = y.strip('\'')

            wcl_list.append(c)

        z_list.append(wcl_list)

    return z_list





if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=443,ssl_context=("fullchain.pem","privkey.pem"))
    #app.run(host='0.0.0.0',debug = True,port=443,ssl_context=("fullchain.pem","privkey.pem"))
    app.run(host='127.0.0.1',port=5000,debug = True)
    #app.run(host='0.0.0.0',port=80)

    #app.run(host='0.0.0.0',debug = True,port=80)

