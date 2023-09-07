from .models import Data,QualifedStudents
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

class DataSchema(SQLAlchemySchema):
    class Meta:
        model = Data

    id = auto_field()
    name = auto_field()
    mobile = auto_field()
    email = auto_field()
    day = auto_field()
    qNo = auto_field()
    status = auto_field()    


class QualifedStudentsSchema(SQLAlchemySchema):
    class Meta:
        model = QualifedStudents
    
    id = auto_field()
    name = auto_field()
    mobile = auto_field()
    email = auto_field()
    day = auto_field()

        
