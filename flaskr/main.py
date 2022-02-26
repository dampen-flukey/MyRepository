
import math
import os
from werkzeug.utils import secure_filename
from turtle import title
from flask_mail import Mail
import json
from datetime import datetime
from sqlalchemy import null
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, url_for, request, session
from unicodedata import name
from enum import unique
from crypt import methods
import pymysql
pymysql.install_as_MySQLdb()

local_server = True  # can also be fetched from config.json file
with open('config.json') as c:
    params = json.load(c)['params']

app = Flask(__name__)
app.secret_key = "super-secret-key"
app.config["UPLOAD_FOLDER"] = params['upload_location']
app.config.update(

    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail_user'],
    MAIL_PASSWORD=params['gmail_password']
)
mail = Mail(app)

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)


class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120))
    phone_num = db.Column(db.String(120))
    msg = db.Column(db.String(120))
    date = db.Column(db.String(120), nullable=True)


class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    slug = db.Column(db.String(25))
    content = db.Column(db.String(120))
    date = db.Column(db.String(120), nullable=True)
    img_file = db.Column(db.String(120), nullable=True)
    subheading = db.Column(db.String(120))
    lower_img = db.Column(db.String(50))


@app.route('/')
def home():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['no_of_posts_to_show_on_home']))
    page = request.args.get('page')  # can use any name instead of page
    if(not str(page).isnumeric()):
        page = 1

    page = int(page)

    posts = posts[(page-1)*int(params['no_of_posts_to_show_on_home']): (page-1)*int(
        params['no_of_posts_to_show_on_home'])+int(params['no_of_posts_to_show_on_home'])]

    if(page == 1):
        next = "/?page="+str((page+1))
        prev = '#'
    elif (page == last):
        next = '#'
        prev = "/?page="+str((page-1))
    else:
        next = "/?page="+str((page+1))
        prev = "/?page="+str((page-1))
    # posts = Posts.query.filter_by().all(
    # )[0:params['no_of_posts_to_show_on_home']]
    return render_template('index.html', params=params, posts=posts, prev=prev, next=next)


@ app.route('/about')
def about():
    return render_template('about.html', params=params)


@ app.route('/login', methods=['GET', 'POST'])
def login():
    posts = Posts.query.filter_by().all()
    if ('user' in session and session['user'] == params['admin_user']):
        posts = Posts.query.filter_by().all()
        last = math.ceil(len(posts)/int(params['no_of_posts_to_show_on_home']))
        page = request.args.get('page')  # can use any name instead of page
        if(not str(page).isnumeric()):
            page = 1

        page = int(page)

        posts = posts[(page-1)*int(params['no_of_posts_to_show_on_home']): (page-1)*int(
            params['no_of_posts_to_show_on_home'])+int(params['no_of_posts_to_show_on_home'])]

        if(page == 1):
            next = "/login?page="+str((page+1))
            prev = '#'
        elif (page == last):
            next = '#'
            prev = "/login?page="+str((page-1))
        else:
            next = "/login?page="+str((page+1))
            prev = "/login?page="+str((page-1))
        return render_template('loginSucess.html', params=params, posts=posts, prev=prev, next=next)

    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('pass')
        if(username == params['admin_user'] and password == params['admin_password']):
            session['user'] = username
            posts = Posts.query.filter_by().all()
            last = math.ceil(
                len(posts)/int(params['no_of_posts_to_show_on_home']))
            page = request.args.get('page')  # can use any name instead of page
            if(not str(page).isnumeric()):
                page = 1

            page = int(page)

            posts = posts[(page-1)*int(params['no_of_posts_to_show_on_home']): (page-1)*int(
                params['no_of_posts_to_show_on_home'])+int(params['no_of_posts_to_show_on_home'])]

            if(page == 1):
                next = "/login?page="+str((page+1))
                prev = '#'
            elif (page == last):
                next = '#'
                prev = "/login?page="+str((page-1))
            else:
                next = "/login?page="+str((page+1))
                prev = "/login?page="+str((page-1))

            return render_template('loginSucess.html', params=params, posts=posts, prev=prev, next=next)
    else:
        return render_template('login.html', params=params)


@ app.route('/contact', methods=['GET', 'POST'])
def contact():
    if(request.method == 'POST'):
        name1 = request.form.get("name")
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contact(name=name1, email=email, phone_num=phone,
                        msg=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        mail.send_message(subject="New message from " + name1, sender=email, recipients=[params['gmail_user']],
                          body=message + "\n"+phone
                          )
    return render_template('contact.html', params=params)


@ app.route('/post/<string:post_slug>', methods=['GET'])
def post_sample(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)


@app.route('/edit/<string:sno>', methods=['GET', 'POST'])
def editPost(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        print('entering')
        print(sno)
        if request.method == 'POST':
            print('post call')
            title = request.form.get('title')
            sub_heading = request.form.get('sub_heading')
            content = request.form.get('content')
            slug = request.form.get('slug')
            img_file = request.form.get('img_file')
            lower_img = request.form.get('lower_img')
            date = datetime.now()

            if sno == '0':
                print('sno == 0')
                post = Posts(title=title, subheading=sub_heading, content=content,
                             slug=slug, img_file=img_file, lower_img=lower_img, date=date)
                db.session.add(post)
                db.session.commit()
                return redirect('/edit/'+sno)
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = title
                post.subheading = sub_heading
                post.content = content
                post.slug = slug
                post.img_file = img_file
                post.lower_img = lower_img
                post.date = date
                # db.session.add(post)
                db.session.commit()
                return redirect('/edit/'+sno)
    post = Posts.query.filter_by(sno=sno).first()
    print('return to edit')
    return render_template('editPost.html', params=params, post=post)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if ('user' in session and session['user'] == params['admin_user']):

        if request.method == 'POST':
            f = request.files['fileupload']
            f.save(os.path.join(
                app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return 'WOHOOOOOOO!!!!!'


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')


@app.route('/delete/<string:sno>', methods=['GET', 'POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        post = Posts.query.filter_by(sno=sno).first()

        db.session.delete(post)
        db.session.commit()
        posts = Posts.query.filter_by().all(
        )[0:params['no_of_posts_to_show_on_home']]
        return redirect('/login')


@app.route('/add/<string:sno>', methods=['GET', 'POST'])
def addPost(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            print('post call')
            title = request.form.get('title')
            sub_heading = request.form.get('sub_heading')
            content = request.form.get('content')
            slug = request.form.get('slug')
            img_file = request.form.get('img_file')
            lower_img = request.form.get('lower_img')
            date = datetime.now()
            if sno == '0':
                print('sno == 0')
                post = Posts(title=title, subheading=sub_heading, content=content,
                             slug=slug, img_file=img_file, lower_img=lower_img, date=date)
                db.session.add(post)
                db.session.commit()
                return redirect('/login')
    post = Posts.query.filter_by(sno=sno).first()
    return render_template('addPost.html', params=params, post=post)


app.run(debug=True)
