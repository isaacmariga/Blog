from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from sqlalchemy.sql import func
from flask import session



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship('Post',backref = 'author',lazy = "dynamic")
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)     

    def __repr__(self):
        return f'User {self.username}'


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    post_image_path  = db.Column(db.String(200), nullable=True)


    comments = db.relationship('Comment', backref='post', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_post(cls):
        posts = Post.query.all()
        return posts



class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment_content = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id") )
    user_id = db.Column(db.Integer, db.ForeignKey("users.id") )

    def save_comment(self):
     
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,post_id):

        comments = Comment.query.filter_by(post_id=post_id).all()

        return comments

class Quote:

  def __init__(self, id, author, quote):
    self.id = id
    self.author = author
    self.quote = quote
