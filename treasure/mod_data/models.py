
from treasure import db
from ..models import Base


class Data(Base):

    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    mobile = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    day = db.Column(db.String(64), nullable=False)
    qNo = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(64), nullable=False)


class QualifedStudents(Base):
    __tablename__ = "qualified_students"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    mobile = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    day = db.Column(db.String(64), nullable=False)
    url = db.Column(db.String(64), nullable=False)
    # is_answered = db.Column(db.Boolean, unique=False, default=False)

class Sentence(Base):
    __tablename__ = 'sentence'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    day =  db.Column(db.String(64), nullable=False)
    sentence = db.Column(db.String(64), nullable=False)