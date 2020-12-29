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
        
        
        newId = registrationsDao.create(values)
        registration['id'] = newId
        
    return render_template('register.html', message=message)
    

@app.route('/login/', methods=['GET', 'POST'])
def login():
    
    error = None
    
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
        account= registrationsDao.findOne(values) 
        # use values from login form to check if account exists
                
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
            # Show the login form with message 
            return render_template('login.html', error = error)
            


@app.route('/students')
def getAll():
    return jsonify(studentDao.getAll())


@app.route('/students/<int:id>')
def findById(id):
    return jsonify(studentDao.findById(id))

# create new student
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
    

#update a students details

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

# delete student from database

@app.route('/students/<int:id>', methods=['DELETE'])
def delete(id):
    studentDao.delete(id)

    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)