from flask import Flask, render_template, request
from connection import Neo4jDatabase


app = Flask(__name__)
uri = "neo4j+s://b76e3d84.databases.neo4j.io:7687"
user = "neo4j"
password = "kH8WQkwu-vK5bmjUYjJ2oe1kbcBeoZdDeErj9o8woSk"


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    return render_template('login.html')


@app.route('/login/superAdmin', methods=['POST'])
def superAdminLogin():
    return render_template('superAdminLogin.html')


@app.route('/login/index', methods=['POST'])
def dashboard():
    user_input = request.form.get('email')
    name = request.form.get('name')
    db = Neo4jDatabase(uri, user, password)
    data = db.match_node(name, user_input)
    if data[0]['name'] == name:
        print('true')
        content = handle_click(name)
        message = f"my name is {name} and my email Id is {user_input}"
        return render_template('assistant.html', content=content, message=message,)
    else:
        return render_template('index.html')


@app.route('/login/SuperAdmin/dashboard', methods=['POST'])
def superAdmin():
    user_input = request.form.get('email')
    name = request.form.get('name')
    print(name, user_input)
    db = Neo4jDatabase(uri, user, password)

    try:
        data = db.Robotic_dashboard(user_input)
        print(data)

        if not data:
            print('hello')
            return render_template('failedSuperAdmin.html')

        if data[0].get('email') == user_input:
            print('true')
            content = handle_click(name)
            message = f"hello {name}"
            return render_template('superAdminDashboard.html', content=content, message=message)

    except Exception as e:
        print(f"An error occurred: {e}")

    print('false')
    return render_template('index.html')


@app.route('/login/SuperAdmin/terminal', methods=['POST'])
def terminal():
    input = request.form.get('input')
    if input == 'hello':
        return 'hello'
    else:
        return 'i dont understand'


@app.route('/home', methods=['POST'])
def home():
    return 'Hello, World!'


@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'


def handle_click(name):
    print(process_input())
    user_input, name, profession = process_input()
    new_content = f'hello {name}'
    return new_content


def process_input():
    user_input = request.form.get('email')
    name = request.form.get('name')
    profession = request.form.get('job')
    print(profession)
    return user_input, name, profession


@app.route('/index', methods=['POST'])
def default():
    title = "personal assistant"
    print(process_input())
    user_input, name, profession = process_input()
    db = Neo4jDatabase(uri, user, password)
    content = db.create_node(name, user_input, profession)
    content = handle_click(name)
    message = f"my name is {name} and i am {profession} and my email Id is {user_input}"
    print(content)
    db.close()
    return render_template('assistant.html', title=title, message=message, content=content)


if __name__ == '__main__':
    app.run(debug=True)
