from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host='db'
    )
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    time = cur.fetchone()
    cur.close()
    conn.close()
    return f"The database time is: {time}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
