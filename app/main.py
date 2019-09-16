import os
from flask import Flask, render_template, session, redirect, url_for, flash,request, g
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required
from flask_login import logout_user, login_user


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
        return "%r*%r*%r" % (self.year,self.describe,self.photo)


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
        return "%r*%r*%r*%r" % (self.name,self.describe,self.photo,self.body)

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


@app.route('/')
def index():
    a = Years.query.all()

    z_list = []

    for x in a:
        a = str(x)
        b = a.split("*")
        wcl_list = []

        for y in b :
            c = y.strip('\'')

            wcl_list.append(c)

        z_list.append(wcl_list)

    return render_template('index.html',lista = z_list)


@app.route('/years/<v>/')
def year(v):
    #年度学期页面生成 self.year,self.describe,self.photo
    #self.activity,self.describe,self.photo
    a = Years.query.filter_by(year=v).first()
    b = Det.query.filter_by(role=a).all()

    z_list = []

    for x in b:
        a = str(x)
        b = a.split("*")
        wcl_list = []

        for y in b :
            c = y.strip('\'')

            wcl_list.append(c)

        z_list.append(wcl_list)


    return render_template('one.html',lista = z_list)



@app.route('/det/<v>/')
def det(v):
    #活动选择 self.name,self.describe,self.photo,self.body)
    det_list = Det.query.filter_by(name=v).first()

    a = str(det_list)
    b = a.split("*")
    wcl_list = []

    for y in b :

        c = y.strip('\'')

        wcl_list.append(c)

    z_list = []
    zw = wcl_list[-1]
    zw = zw.split("∂")
    for x in zw:
        x = x.split("ƒ")
        z_list.append(x)


    return render_template('det.html',lista = z_list)




def two_list_chuli(a):

    z_list = []

    for x in a:
        a = str(x)
        b = a.split("*")
        wcl_list = []

        for y in b :
            c = y.strip('\'')

            wcl_list.append(c)

        z_list.append(wcl_list)

    return z_list




@app.route('/api/',methods=['POST','GET'])
def apidk():
    text=request.args.get('config')
    if text is not None:
        a = str(text)
        d = a.strip("\"")
        zlist = d.split("å")

        if zlist[0] == "update":
            if zlist[1] == "year":
                #“update å years å year_name å describe å photo_path”
                tjb = Years(year = zlist[2],describe = zlist[3],photo = zlist[4])
                db.session.add(tjb)
                db.session.commit()


            if zlist[1] == "det":
                #“update å det å det_name å describe å photo_path å body å act_id”
                a = Years.query.filter_by(year=zlist[6]).first()
                tjb = Det(name = zlist[2],describe = zlist[3],photo = zlist[4],body=zlist[5],role=a)
                db.session.add(tjb)
                db.session.commit()
                '''
        if zlist[0] == "delete":
            if zlist[1] == "year":


            if zlist[1] == "det":
                '''

        if zlist[0] == "search":

            if zlist[1] == "year":

                a = Years.query.all()

                return two_list_chuli(a)


            if zlist[1] == "det":

                a = Det.query.all()

                return two_list_chuli(a)




@app.route("/api/upload/",methods=['POST','GET'])
def upjpg():

    upload_file = request.files['file']
    
    old_file_name = upload_file.filename
    yz_name = old_file_name.split("!")

    if upload_file:

        if yz_name == "year_min":
            file_path = os.path.join("hlby_web/static/img/year_min/", old_file_name)
            upload_file.save(file_path)

        if yz_name == "det_min":
            file_path = os.path.join("hlby_web/static/img/det_min/", old_file_name)
            upload_file.save(file_path)

        if yz_name == "det":
            file_path = os.path.join("hlby_web/static/img/det/", old_file_name)
            upload_file.save(file_path)
        
        return '发送完成'
    else:
        return '发送失败'

'''


@app.route('/api/',methods=['POST','GET'])
def apidk():
    text=request.args.get('config')
    if text is not None:
        a = str(text)
        d = a.strip("\"")
        b = d.split("å")
        actname = b[0]
        actms = b[1]
        actfile = b[2]
        photonamew = b[3]
        
        sss = photonamew.split("!")

        aa = Act(activity=actname,describe=actms,file_wjj=actfile,hphoto=sss[0])

        db.session.add(aa)
        js = 0
        for x in sss:
            js += 1

            exec(f"a{js} = Potx(photoname=\"{x}\",describe=\"无描述\",role=aa)")

            exec(f"db.session.add(a{js})")
        
        db.session.commit()

        
    return str(sss)


@app.route('/api/del/',methods=['POST','GET'])
def apidel():
    text=request.args.get('f')
    if text is not None:
        text = text.split("!")

        if text[0] == "qaswazxs":

            aa = Act.query.filter_by(file_wjj=text[1]).first()
            db.session.delete(aa)            
            db.session.commit()
        else:
            return "口令错误！"

        
    return "删除完成!"
'''

if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=443,ssl_context=("fullchain.pem","privkey.pem"))
    #app.run(host='0.0.0.0',debug = True,port=443,ssl_context=("fullchain.pem","privkey.pem"))
    #app.run(host='127.0.0.1',port=80,debug = True)
    app.run(host='0.0.0.0',port=80)

    #app.run(host='0.0.0.0',debug = True,port=80)

