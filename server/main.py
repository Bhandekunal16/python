from flask import Flask, render_template, request
from connection import GraphDatabase
import connection
from retrying import retry

app = Flask(__name__)

uri = "neo4j+s://b76e3d84.databases.neo4j.io:7687"
user = "neo4j"
password = "kH8WQkwu-vK5bmjUYjJ2oe1kbcBeoZdDeErj9o8woSk"


class Neo4jDatabase:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def create_node(self, name, email, profession):
        with self._driver.session() as session:
            result = session.write_transaction(
                self._create_node, name, email, profession)
        return result

    @staticmethod
    def _create_node(tx, name, email, profession):
        query = (
            "CREATE (n:Person {name: $name, email: $email, profession: $profession})"
            "RETURN id(n)"
        )
        result = tx.run(query, name=name, email=email, profession=profession)
        return result.single()[0]


# Retry 3 times with a 1-second delay between retries
@retry(stop_max_attempt_number=3, wait_fixed=1000)
def connect_to_neo4j():
    # Your code to connect to Neo4j here
    pass


try:
    connect_to_neo4j()
except connection.exceptions.ServiceUnavailable:
    print("Failed to connect to Neo4j after multiple retries.")

@app.route('/')
def hello_world():
    return 'hello'

@app.route('/')
def hello_world():
    return render_template('index.html')


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
