from flask import Flask,redirect,render_template,request,session,url_for,jsonify
from Forms import login,sinUp
from  FirebasePackage.Firebase import firebase
import sqlite3
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime


app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)
base_dir = os.path.dirname(__file__)
database = "sqlite:///" + os.path.join(base_dir, "data.sqlite")
app.config["SQLALCHEMY_DATABASE_URI"] = database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
Migrate(app, db)

FB = firebase()




@app.route('/',methods=['GET'])
def welcome():
    if 'usr' in session:
        return redirect(url_for('home'))
    else:
        return render_template('welcome.html')

@app.route('/sinup', methods=['POST'])
def sinup():
    if request.method == "POST":
        _username = request.form['username']
        _password = request.form['password']
        isFlag, usr = FB.Signup(name="藤季", email=_username, password=_password)
        if isFlag:
            session["usr"] = usr.uid
            print(session["usr"])
            create_user(usr.uid, "藤季", _username)
            return redirect(url_for('Introduction'))
        else:
            return render_template('welcome.html', sinup_failed=not isFlag, sinup_error=usr)
    else:
        return render_template('welcome.html')
    
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        _username = request.form['username']
        _password = request.form['password']
        isFlag, usr = FB.Login(email=_username, password=_password)
        if isFlag:
            session['usr'] = _username
            return redirect(url_for('home'))
        else:
            return render_template('welcome.html', login_failed = not isFlag ,login_error='ユーザ名またはパスワードが間違っています')
    else:
        return render_template('welcome.html')

@app.route('/logout')
def logout():
    session.pop('usr', None)
    return redirect(url_for('welcome'))

@app.route('/home')
def home():
    if "usr" in session:
        return render_template('home.html')
    else:
        return render_template('welcome.html')

@app.route('/introduction')
def Introduction():
    return render_template('Introduction.html')

@app.route('/introduction2')
def introduction2():
    return render_template('Introduction2.html')

@app.route('/save-preference', methods=['POST'])
def save_preference():
    data = request.get_json()
    category = data['category']
    preference = data['preference']
    
    # ここでデータベースに接続し、データを保存
    conn = sqlite3.connect('preferences.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS preferences (id INTEGER PRIMARY KEY, category TEXT, preference TEXT)")
    c.execute("INSERT INTO preferences (category, preference) VALUES (?, ?)", (category, preference))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success'})



# ユーザーテーブル
class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    closet_items = db.relationship('Closet', backref='owner', lazy='dynamic')
    favorite_styles = db.relationship('Style', secondary='user_style_link', back_populates='users')

# クローゼットテーブル
class Closet(db.Model):
    __tablename__ = 'closet'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(50), db.ForeignKey('user.uid'), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(50))
    image = db.Column(db.String(100), nullable=False)
    clothes_styles = db.relationship('Style', secondary='closet_style_link', back_populates='closets')
    #オプションのカラム
    size = db.Column(db.String(50))
    price = db.Column(db.Float)
    purchase_date = db.Column(db.DateTime)
    note = db.Column(db.Text)

# フォロワーテーブル
class Follower(db.Model):
    __tablename__ = 'follower'
    id = db.Column(db.Integer, primary_key=True)
    follower_uid = db.Column(db.String(50), db.ForeignKey('user.uid'), nullable=False)
    followed_uid = db.Column(db.String(50), db.ForeignKey('user.uid'), nullable=False)

# スタイルテーブル
class Style(db.Model):
    __tablename__ = 'style'
    id = db.Column(db.Integer, primary_key=True)
    style_name = db.Column(db.String(50), nullable=False)
    users = db.relationship('User', secondary='user_style_link', back_populates='favorite_styles')
    closets = db.relationship('Closet', secondary='closet_style_link', back_populates='clothes_styles')

# ユーザーとスタイルの中間テーブル
user_style_link = db.Table('user_style_link',
    db.Column('user_id', db.Integer, db.ForeignKey('user.uid', name='fk_user_style_user_id'), primary_key=True),
    db.Column('style_id', db.Integer, db.ForeignKey('style.id', name='fk_user_style_style_id'), primary_key=True)
)

# クローゼットとスタイルの中間テーブル
closet_style_link = db.Table('closet_style_link',
    db.Column('closet_id', db.Integer, db.ForeignKey('closet.id', name='fk_closet_style_closet_id'), primary_key=True),
    db.Column('style_id', db.Integer, db.ForeignKey('style.id', name='fk_closet_style_style_id'), primary_key=True)
)

    
def create_user(uid,name, email):
    with app.app_context():
        user = User(uid=uid, name=name, email=email)
        db.session.add(user)
        db.session.commit()
        print("成功")

def create_closet(user_uid, category, brand, image, style, size=None, price=None, purchase_date=None, note=None):
    with app.app_context():
        closet = Closet(user_uid=user_uid, category=category, brand=brand, image=image, style=style, size=size, price=price, purchase_date=purchase_date, note=note)
        db.session.add(closet)
        db.session.commit()
        return closet

def create_follower(follower_uid, followed_uid):
    with app.app_context():
        follower = Follower(follower_uid=follower_uid, followed_uid=followed_uid)
        db.session.add(follower)
        db.session.commit()
        return follower


if __name__ == '__main__':
    app.run(debug=True)

