from treasure import db
import os
from datetime import time, datetime
from .models import Data, QualifedStudents
from .schemas import DataSchema, QualifedStudentsSchema
from flask import Blueprint, flash, g, redirect, request, session, make_response, jsonify
from datetime import datetime, date
import uuid
from ..new_mailsetup import email_send
# from  ...config import url_vm
url_vm = 'http://143.110.244.231/'
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

            #  checking whether the student already has completed the question or not

            eixisting_record = Data.query.filter_by(name=name,email=email,mobile=mobile,qNo=qNo,day=day).first()

            if eixisting_record:
                print('record found')
                eixisting_record.name = name
                eixisting_record.email = email
                eixisting_record.mobile = mobile
                eixisting_record.qNo = qNo
                eixisting_record.status = status
                eixisting_record.day = day

                db.session.commit()


            else:

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
            if len(data) == 10 and not QualifedStudents.query.filter_by(name=name,email=email,mobile=mobile,day=day).first():
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
                # email_send(email,4,'')


            path = '/var/www/html/' + str(url)

            # check whether directory already exists
            if not os.path.exists(path):
                 os.mkdir(path)
                 print("Folder %s created!" % path)
            else:
                print("Folder %s already exists" % path)


            # Creating the HTML file
            file_name = path + '/' + name + ".html"
            file_html = open(file_name, "w")

            # Adding the input data to the HTML file
            file_html.write('''<html>
            <head>
            <title>Student Details</title>
            </head> 
            <body>
                email:{{email}}
                    
            <h1>Welcome </h1>           
            <p>Example demonstrating How to generate HTML Files in Python</p>
                            
            <h2> Sentence Validation</h2>

            <p>Please input the sentence after combining all the words:</p>

            <input id="numb">

            <button type="button" onclick="myFunction()">Submit</button>

            <p id="demo"></p>

            <script>
            function myFunction() {
            // Get the value of the input field with id="numb"
            let x = document.getElementById("numb").value;
            let y = 'This is The Best Course On This Planet At Present';
            // If x is Not a Number or less than one or greater than 10
            let text;
            if (x==y) {
                text = "correct Answer";
            } else {
                text = "Incorrect Answer please try again";
            }
            document.getElementById("demo").innerHTML = text;
            }
            </script>
                             
            </body>
                                 
            </html>''')

            # Saving the data into the HTML file
            file_html.close()
            url_to_send = url_vm + str(url) + '/' + name + '.html'
            email_send(email,4,url_to_send)
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
