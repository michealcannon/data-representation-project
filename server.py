from flask import Flask, jsonify, request, abort, render_template, redirect, url_for, session, flash
from RegistrationsDao import registrationsDao
from StudentDao import studentDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return render_template('landing_page.html') 

@app.route('/register/', methods=['post', 'get'])
def register():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')  # access the data inside 
        password = request.form.get('password')
        registration = {
            "username": username,
            "password": password
        }
        values =(registration['username'],registration['password'])
        
        # if username == 'root' and password == 'pass':
        #     message = "Correct username and password"
        # else:
        #     message = "Wrong username or password"
        newId = registrationsDao.create(values)
        registration['id'] = newId
        return jsonify(registration)
    return render_template('register.html', message=message)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # return render_template('login.html', msg='')
        # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST':
        username = request.form.get('username')  # access the data inside 
        password = request.form.get('password')
        # Create variables for easy access
        login = {
            "username": username,
            "password": password
        }
        values =(login['username'],login['password'])
        # return jsonify(values)
        account= registrationsDao.findOne(values)
        # return jsonify(account)
                # If account exists in accounts table in out database
        if account:
            return redirect("/index.html")
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            print('Logged in successfully!')
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)

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