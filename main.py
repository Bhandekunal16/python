from flask import Flask, render_template,jsonify, Request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'


@app.route('/handle_click', methods=['POST'])
def handle_click():
    new_content = "Content updated after clicking the button."
    return new_content


@app.route('/index')
def index():
    title = "resume"
    content= handle_click()
    message = "my name is kunal and i am software developer"
    name = "kuanl"
    print(content)
    return render_template('home.html', title=title, message=message, name=name, content=content)


if __name__ == '__main__':
    app.run(debug=True)
