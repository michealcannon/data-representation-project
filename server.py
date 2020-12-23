from flask import Flask, url_for, request, redirect, abort, jsonify
from StudentDao import studentDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return "hello"

@app.route('/register/', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        # Create variables for easy access
        email = request.form['email']
        password = request.form['password']
        registration = registrationsDAO.fetchone()
        
        registrationsDao.create()
    
    return render_template('register.html', msg=msg)

#get all
# curl http://127.0.0.1:5000/students

@app.route('/students')
def getAll():
    return jsonify(studentDao.getAll())


# find By id
# curl http://127.0.0.1:5000/student/2

@app.route('/students/<int:id>')
def findById(id):
    return jsonify(studentDao.findById(id))

# create
# curl -X POST -d "{\"first_name\":\"john\", \"surname\":\"doe\", \"grade\":70, \"absences\":2}" -H Content-Type:application/json http://127.0.0.1:5000/students

@app.route('/students', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)

    student = {
        
        "first_name": request.json["first_name"],
        "surname": request.json["surname"],
        "grade": request.json["grade"],
        "absences": request.json["absences"]
    }
    values =(student['first_name'],student['surname'],student['grade'], student['absences'])
    newId = studentDao.create(values)
    student['id'] = newId
    return jsonify(student)
    

#update
# curl -X PUT -d "{\"first_name\":\"Jane\", \"grade\":80}" -H "content-type:application/json" http://127.0.0.1:5000/students/1


@app.route('/students/<int:id>', methods=['PUT'])
def update(id):
    foundStudent=studentDao.findById(id)
    print (foundStudent)
    if foundStudent == {}:
        return jsonify({}), 404
    currentStudent = foundStudent
    if 'first_name' in request.json:
        currentStudent['first_name'] = request.json['first_name']
    if 'surname' in request.json:
        currentStudent['surname'] = request.json['surname']
    if 'grade' in request.json:
        currentStudent['grade'] = request.json['grade']
    if 'absences' in request.json:
        currentStudent['absences'] = request.json['absences']
    values =(currentStudent['first_name'],currentStudent['surname'],currentStudent['grade'], currentStudent['absences'], currentStudent['id'])
    studentDao.update(values)

    return jsonify(currentStudent)

#delete
# curl -X DELETE http://127.0.0.1:5000/students/1


@app.route('/students/<int:id>', methods=['DELETE'])
def delete(id):
    studentDao.delete(id)

    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)