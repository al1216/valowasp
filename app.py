from enum import unique
from logging import debug
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import PrimaryKeyConstraint
from sqlalchemy import String, create_engine, MetaData, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

app=Flask(__name__)

Base = declarative_base()


app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:saritamanas@localhost/valo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

# engine = create_engine('mysql+pymysql://root:saritamanas@127.0.0.1/valo')
# metadata = MetaData(bind=engine)
# Base = declarative_base(metadata=metadata)


# User = Table(
#     "user",
#     Base.metadata,
#     Column("discord_id", Integer, ForeignKey("author.author_id")),
#     Column("valorant_id", Integer, ForeignKey("publisher.publisher_id")),
#     Column("player_level",String(100)),
#     Column("email_id",String(100)),
#     Column("contact_no",String(12))
# )


class member(db.Model):
    __tablename__ = 'table1'


    discord_id=db.Column(String(100),primary_key=True)
    valorant_id=db.Column(String(100),unique=True)
    player_level=db.Column(String(100))
    email_id=db.Column(String(100),unique=True)
    contact_no=db.Column(String(12))

    def __repr__(self):
        return '<Discord_id %r>' % self.discord_id

class form(db.Model):
    __tablename__='table2'


    id=db.Column(db.Integer,primary_key=True)
    team_name=db.Column(db.String(100),unique=True)
    email_id=db.Column(db.String(100),unique=True)
    contact_no_lead=db.Column(db.String(100))
    no_members=db.Column(db.Integer)

    def __repr__(self):
        return '<Id %r>' % self.id



@app.route('/')
def index():
    return render_template('index.html')

if __name__== '__main__':
    app.run(debug=True)