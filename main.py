from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome"

employees = [{
                "userId": "rirani",
                "jobTitleName": "Developer",
                "firstName": "Romin",
                "lastName": "Irani",
                "preferredFullName": "Romin Irani",
                "employeeCode": "E1",
                "region": "CA",
                "phoneNumber": "408-1234567",
                "emailAddress": "romin.k.irani@gmail.com"
            },
            {
                "userId": "nirani",
                "jobTitleName": "Developer",
                "firstName": "Neil",
                "lastName": "Irani",
                "preferredFullName": "Neil Irani",
                "employeeCode": "E2",
                "region": "CA",
                "phoneNumber": "408-1111111",
                "emailAddress": "neilrirani@gmail.com"
            },
            {
                "userId": "thanks",
                "jobTitleName": "Program Directory",
                "firstName": "Tom",
                "lastName": "Hanks",
                "preferredFullName": "Tom Hanks",
                "employeeCode": "E3",
                "region": "CA",
                "phoneNumber": "408-2222222",
                "emailAddress": "tomhanks@gmail.com"
            }]

@app.route('/')

@app.route('/employees', methods = ['GET'])
def get():
    return jsonify({'Employees':employees})
@app.route('/employees/<int:firstName>', methods = ['GET'])
# <int:firstName> ---> Since we Provide Index, So Always Fetch Data through Index Only : Example as : /employees/0 OR /employees/1 Will Fetch Data for that Index {Compulsory to use firstName [Def] Only

def get_names(firstName):
    return jsonify({'Name':employees[firstName]})

@app.route('/employees/', methods = ['POST'])
def create():
    employee_new = {
                "userId": "javed",
                "jobTitleName": "Data Analyst",
                "firstName": "Md Javed",
                "lastName": "Momin",
                "preferredFullName": "Md Javed Momin",
                "employeeCode": "E5",
                "region": "IN",
                "phoneNumber": "405-2222222",
                "emailAddress": "javedmomin99@gmail.com"
    }
    employees.append(employee_new)
    return jsonify({'Created':employee_new})
@app.route('/employees/<int:firstName>', methods = ['PUT'])
def job_update(firstName):
    employees[firstName]['jobTitleName'] = "Data Engineer"
    return jsonify({'employees':employees[firstName]})

@app.route('/employees/<int:firstName>', methods = ['DELETE'])
def delete(firstName):
    employees.remove(employees[firstName])
    return jsonify({'result' : True})

# Write in Terminal to get O/P:
# curl.exe -i -H "Content-Type:Application/json" -X GET http://localhost:5000/employees/
# curl.exe -i -H "Content-Type:Application/json" -X POST http://localhost:5000/employees/
# curl.exe -i -H "Content-Type:Application/json" -X PUT http://localhost:5000/employees/
# curl.exe -i -H "Content-Type:Application/json" -X DELETE http://localhost:5000/employees/
# curl.exe -i -H "Content-Type:Application/json" -X GET http://localhost:5000/employees/0
# curl.exe -i -H "Content-Type:Application/json" -X POST http://localhost:5000/employees/1
# curl.exe -i -H "Content-Type:Application/json" -X PUT http://localhost:5000/employees/2
# curl.exe -i -H "Content-Type:Application/json" -X DELETE http://localhost:5000/employees/3




if __name__ == "__main__":
    app.run(debug=True)