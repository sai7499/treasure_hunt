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

            eixisting_record = Data.query.filter_by(
                name=name, email=email, mobile=mobile, qNo=qNo, day=day).first()

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
                print('record not found')

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

            print('***uuid starts here******')
            url = uuid.uuid4()
            print(url)
            print('****uuid ends here*****')

            #  checking whether the student completes all the question or not respective to particular day

            records = db.session.query(
                Data.name, Data.mobile, Data.email, Data.qNo, Data.day).filter_by(mobile=mobile, day=day).all()

            data_schema = DataSchema()
            data = data_schema.dump(records, many=True)

            print(len(data),'data')


            # checking if user completes all the questions starts here 
            if len(data) == 10 and not QualifedStudents.query.filter_by(name=name, email=email, mobile=mobile, day=day).first():
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

<body>
    <h1>Welcome </h1>

    <h1 id="student_name"></h1>



    <!-- <h2> Sentence Validation</h2> -->


    <form>
        
        <label for="name">First name:</label><br>
        <input type="text" id="name" name="name" disabled><br>
        <label for="email">email:</label><br>
        <input type="text" id="email" name="email" disabled><br><br>
        <label for="mobile">mobile:</label><br>
        <input type="text" id="mobile" name="mobile" disabled><br><br>
    </form>

    <p>Please input the sentence after combining all the words:</p>

    <input id="numb">

    <button type="button" onclick="myFunction()">Submit</button>
    <p id="demo"></p>

    <script>
        // disp = false
        function submit(){
            alert('name')
        }

        function myFunction() {
            // Get the value of the input field with id="numb"
            let x = document.getElementById("numb").value;
            let y = 'This is The Best Course On This Planet At Present';

            let text;
            if (x == y) {
                text = "correct Answer";
            } else {
                text = "Incorrect Answer please try again";
            }
            document.getElementById("demo").innerHTML = text;
        }

        var path = window.location.pathname;
        var page = path.split("/").pop();
        var stu_name = page.split(".")[0]
        console.log('student name == ', stu_name);
        document.getElementById("student_name").innerHTML = stu_name;

        url = "http://143.110.244.231:5002/treasure_hunt/getDetails"



        async function UserAction() {
            const data = { name: stu_name };
            try {
                const response = await fetch(url, {
                    method: "POST", // or 'PUT'
                    headers: {
                        "Content-type": "application/json",
                    },
                    body: JSON.stringify(data),
                });

                const result = await response.json();
                name = result['data']['name']
                email = result['data']['email']
                mobile = result['data']['mobile']
                document.getElementById("name").innerHTML = name;
                document.getElementById("email").innerHTML = email;
                document.getElementById("mobile").innerHTML = mobile;
                // disp = false
                console.log("Success:", mobile);
            } catch (error) {
                console.error("Error:", error);
            }
        }
        UserAction()


    </script>

</body>

</html>''')


                # Saving the data into the HTML file
                file_html.close()
                url_to_send = url_vm + str(url) + '/' + name + '.html'

                # sending an email to the respective admin about the user actions
                email_send(email, 4, url_to_send)

                # checking if user completes all the questions ends here 
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


# api to get the student data based on student name

@mod_data.route("/getDetails",methods=("GET", "POST"))
def getDetails():
    print('request',request)
    if request.method == "POST":
            name = request.json['name']
            print('request',request.json['name'])
            # name = 'test'
            # print('name',name)
            existing_record = Data.query.filter_by(
                name=name).first()

            if existing_record :

                print('record found')

                stu_email = existing_record.email
                stu_mobile = existing_record.mobile
                
            else :
                print('record not found')
                res_data = {'email': '','name':name,'mobile':''}
                return make_response(
                jsonify(
                    {
                        "status": "fail",
                        # "message": "data fetched successfully",
                        "data": res_data
                    }
                )
            )
                
                
            res_data = {'email': stu_email,'name':name,'mobile':stu_mobile}
            print(res_data)
            return make_response(
                jsonify(
                    {
                        "status": "success",
                        # "message": "data fetched successfully",
                        "data": res_data
                    }
                )
            )
            

    return make_response(
        jsonify({"status": "fail", "message": "Check method type.", "data": ""})
    )
    