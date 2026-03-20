from flask import Flask, jsonify
import pymysql
import os

app = Flask(__name__)

# Read DB credentials from environment variables
DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/")
def home():
    return "Deployed via CI/CD 🚀"

@app.route("/users")
def get_users():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users;")
            result = cursor.fetchall()
        return jsonify(result)
    finally:
        connection.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
