from flask import Flask, render_template, jsonify, Request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/home', methods=['POST'])
def home():
    return 'Hello, World!'


@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'


def handle_click(name):
    new_content = f'hello {name}'
    return new_content


@app.route('/index')
def default():
    title = "resume"
    content = handle_click('unknown')
    message = f"my name is kunal and i am software developer"
    name = "kuanl"
    print(content)
    return render_template('home.html', title=title, message=message, name=name, content=content)

@app.route('/index/<user>')
def index(user):
    title = "resume"
    content = handle_click(user)
    message = f"my name is {user} and i am software developer"
    print(content)
    return render_template('home.html', title=title, message=message, content=content)


if __name__ == '__main__':
    app.run(debug=True)
