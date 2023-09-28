from neo4j import GraphDatabase
import neo4j
from retrying import retry


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

    def match_node(self, name, email):
        with self._driver.session() as session:
            result = session.write_transaction(self._match_node, name, email)
        return result

    def Robotic_dashboard(self, email):
        with self._driver.session() as session:
            result = session.write_transaction(self._Robotic_dashboard, email)
        return result

    @staticmethod
    def _create_node(tx, name, email, profession):
        query = (
            "merge (n:Person {name: $name, email: $email, profession: $profession})"
            "RETURN id(n)"
        )
        result = tx.run(query, name=name, email=email, profession=profession)
        return result.single()[0]

    def _match_node(self, tx, name, email):
        query = (
            "MATCH (n:Person {name: $name, email: $email})"
            "RETURN n"
        )
        result = tx.run(query, name=name, email=email)
        records = result.data()

        if records:
            nodes = [record['n'] for record in records]
            print("Matched nodes:", nodes[0]['name'])
            return nodes
        else:
            print("No matching nodes found.")

    def _Robotic_dashboard(self, tx, email):
        query = (
            "match (n:user {email: $email}) return n"
        )
        result = tx.run(query, email=email)
        records = result.data()

        if records:
            nodes = [record['n'] for record in records]
            print("Matched nodes:", nodes[0]['name'])
            return nodes
        else:
            msg = "none"
            print("No matching nodes found.")
            return msg


@retry(stop_max_attempt_number=3, wait_fixed=1000)
def connect_to_neo4j():
    # Your code to connect to Neo4j here
    pass


try:
    connect_to_neo4j()
except neo4j.exceptions.ServiceUnavailable:
    print("Failed to connect to Neo4j after multiple retries.")
