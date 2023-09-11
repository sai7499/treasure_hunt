from treasure import db
from datetime import time, datetime
from .models import Data, QualifedStudents
from .schemas import DataSchema, QualifedStudentsSchema
from flask import Blueprint, flash, g, redirect, request, session, make_response, jsonify
from datetime import datetime, date
import uuid
from ..new_mailsetup import email_send
mod_data = Blueprint('data', __name__, url_prefix='/treasure_hunt')

# student input data


@mod_data.route("/submit", methods=("GET", "POST"))
def submitData():

    if request.method == "POST":

        try:
            name = request.form['name']
            mobile = request.form['mobile']
            email = request.form['email']
            qNo = int(request.form['qNo'])
            status = request.form['status']

            if qNo < 10 or qNo == 10:
                day = "DAY_1"
            elif qNo < 20 or qNo == 20:
                day = "DAY_2"

        except Exception as e:
            return make_response(
                jsonify({"status": "fail", "message": str(e), "data": ""})

            )
        error = None
        if (email is None or name is None or mobile is None or qNo is None or status is None):
            error = "Please enter all required fields."

        elif error is None:
            record = Data(
                name=name,
                mobile=mobile,
                email=email,
                qNo=qNo,
                status=status,
                day=day
            )
            db.session.add(record)
            db.session.commit()

            print('*********')
            url = uuid.uuid4()
            print(url)
            print('*********')

            #  checking whether the student completes all the question or not respective to particular day

            records = db.session.query(
                Data.name, Data.mobile, Data.email, Data.qNo, Data.day).filter_by(mobile=mobile, day=day).all()
            data_schema = DataSchema()
            data = data_schema.dump(records, many=True)

            # print(len(data))
            if len(data) == 10:
                print("pushing data to qualified table")

                qualifed_data = QualifedStudents(
                    name=data[0]['name'],
                    email=data[0]['email'],
                    mobile=data[0]['mobile'],
                    day=data[0]['day'],
                    # url = name[:2] + email[:2] + mobile[:3] + day
                    url=str(uuid.uuid4()),
                    # print(url)
                )
                db.session.add(qualifed_data)
                db.session.commit()
                email_send(email,4,'')
            return make_response(
                jsonify(
                    {
                        "status": "success",
                        "message": "submitted successfully",
                        "data": "",
                        # "token": token,
                    }
                )
            )

        elif error is not None:
            return make_response(
                jsonify({"status": "fail", "message": error, "data": ""})
            )

    return make_response(
        jsonify({"status": "fail", "message": "Check method type.", "data": ""})
    )
