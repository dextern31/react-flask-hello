from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    firstName = db.Column(db.String)
    lastName = db.Column(db.String)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "firstName": self.firstName,
            "lastName": self.lastName,
            # do not serialize the password, its a security breach
        }
    
class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String, nullable=False)
    stay = db.Column(db.String, nullable=False)
    foodDrinks = db.Column(db.String, nullable=False)
    activities = db.Column(db.String, nullable=False)
    transportation = db.Column(db.String, nullable=False)
    tips = db.Column(db.String, nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship("User")

    def serialize(self):
        #comments = list(map(lambda x: x.serialize(), self.user))
        return {
            "id": self.id,
            "location": self.location,
            "stay": self.stay,
            "foodDrinks": self.foodDrinks,
            "activities": self.activities,
            "transportation": self.transportation,
            "tips": self.tips,
            "userID": self.userID
        }
    

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    comment = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), nullable=False)
    post = db.relationship("Post")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship("User")

    def serialize(self):
        return {
            "id": self.id,
            "comment": self.comment,
            "post_id": self.post_id,
            "user_id": self.user_id
        }

class Friends(db.Model):
    __tablename__ = 'friends'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    user = db.relationship("User", foreign_keys=[user_id])
    friends = db.relationship("User", foreign_keys=[friend_id])


    
