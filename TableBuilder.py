from database import DatabaseConnection
from config import DB_CONFIG

class TableBuilder:
    def __init__(self, db_connection):
        self.db = db_connection

    def create_tables(self):
        commands = [
            '''
            CREATE TABLE IF NOT EXISTS motherboard (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL NOT NULL,
                form VARCHAR(50) NOT NULL,
                soket VARCHAR(50) NOT NULL,
                type_member VARCHAR(50) NOT NULL,
                interface VARCHAR(50) NOT NULL
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS supply (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL NOT NULL,
                power INT NOT NULL,
                type VARCHAR(50) NOT NULL
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS gpu (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL NOT NULL,
                frequency INT NOT NULL,
                soket VARCHAR(50) NOT NULL,
                power_use INT NOT NULL
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS ram (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL NOT NULL,
                frequency INT NOT NULL,
                type_member VARCHAR(50) NOT NULL,
                power_use INT NOT NULL
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS cpu (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL NOT NULL,
                soket VARCHAR(50) NOT NULL,
                frequency INT NOT NULL,
                power_use INT NOT NULL
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS cooler (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL NOT NULL,
                speed INT NOT NULL,
                power_use INT NOT NULL
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS frame (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL NOT NULL,
                form VARCHAR(50) NOT NULL
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS hdd (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL NOT NULL,
                capacity INT NOT NULL,
                recording INT NOT NULL,
                reading INT NOT NULL
            )
            '''
        ]

        for command in commands:
            self.db.execute_query(command)
            print(f"Executed: {command}")

if __name__ == "__main__":
    db_connection = DatabaseConnection(**DB_CONFIG)
    table_builder = TableBuilder(db_connection)
    table_builder.create_tables()
    db_connection.close()
