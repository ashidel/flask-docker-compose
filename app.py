from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    conn = mysql.connector.connect(
        host='db',         # docker-compose.yml में जो service का नाम है
        user='root',
        password='mypass',
        database='mydb'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from Flask + MySQL' AS msg")
    result = cursor.fetchone()
    return result[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
