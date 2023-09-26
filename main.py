from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/index')
def index():
    title = "Title"
    message = "This content was rendered on the server side using Flask and Jinja2."
    
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Server-Side Rendering Example</title>
    </head>
    <body>
        <h1 style="text-align : center;">{{ title }}</h1>
        <p>{{ message }}</p>
    </body>
    </html>
    """
    
    return render_template_string(html_template, title=title, message=message)

if __name__ == '__main__':
    app.run(debug=True)
