from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('form.html')


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
    content = handle_click(name)
    message = f"my name is {name} and i am {profession}, and my email is {user_input}"
    print(content)
    return render_template('index.html', title=title, message=message, content=content)


if __name__ == '__main__':
    app.run(debug=True)
