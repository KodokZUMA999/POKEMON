from flask_bcrypt import Bcrypt
from flask_login import UserMixin

from application import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

bcrypt = Bcrypt()

class FavoritePokemon(db.Model):
    __tablename__ = "favorite_pokemon"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    pokemon_id = db.Column(db.Integer, nullable=False)


class User(db.Model, UserMixin):
    __tablename__   = "users"
    id              = db.Column(db.Integer, primary_key = True)
    username        = db.Column(db.String(128), nullable = False)
    password        = db.Column(db.String(128), nullable = False)
    fullname        = db.Column(db.String(128), nullable = False)
    email           = db.Column(db.String(128), nullable = False)
    profile_pic     = db.Column(db.String(128), default="default.jpg")
    bio             = db.Column(db.String(128))
    join_date       = db.Column(db.DateTime, default=datetime.utcnow)
    status          = db.Column(db.Boolean, default=True)
    following_users = db.relationship("Relation", foreign_keys="Relation.id_following", backref="following", lazy=True)
    follower_users  = db.relationship("Relation", foreign_keys="Relation.id_follower", backref="follower", lazy=True)
    posts           = db.relationship("Post", backref="posts_owner", lazy=True)
    comments        = db.relationship("Comment", backref="comments_owner", lazy=True)
    likes           = db.relationship("Like", backref="likes_owner", lazy=True)

class Relation(db.Model):
    __tablename__   = "relations"
    id              = db.Column(db.Integer, primary_key = True)
    id_follower     = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    id_following    = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    status          = db.Column(db.Boolean, default=True)
    relation_date   = db.Column(db.DateTime, default=datetime.utcnow)

class Post(db.Model):
    __tablename__   = "posts"
    id              = db.Column(db.Integer, primary_key = True)
    author_id       = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    photo = db.Column(db.Text, nullable=False)
    caption         = db.Column(db.String(128), default="")
    status          = db.Column(db.Boolean, default=True)
    post_date       = db.Column(db.DateTime, default=datetime.utcnow)
    comments        = db.relationship("Comment", backref="commented", lazy=True)
    likes           = db.relationship("Like", backref="liked", lazy=True)


class Comment(db.Model):
    __tablename__   = "comments"
    id              = db.Column(db.Integer, primary_key = True)
    text            = db.Column(db.Text, nullable = False)
    commenter_id    = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id         = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    hidden          = db.Column(db.Boolean, default=False)
    comment_date    = db.Column(db.DateTime, default=datetime.utcnow)

class Like(db.Model):
    __tablename__   = "likes"
    id              = db.Column(db.Integer, primary_key = True)
    user_id         = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    post_id         = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable = False)
    status          = db.Column(db.Boolean, default=True)
    like_date       = db.Column(db.DateTime, default=datetime.utcnow)
