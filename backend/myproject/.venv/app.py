from flask import Flask
import psycopg2

app = Flask(__name__)

#ESTABILISH A CONNECTION TO THE PostgreSQL Database
conn = psycopg2.connect(
    host = "localhost",
    database = "Shop",
    user = "postgres",
    password = "13172505"
)

@app.route("/")
def index():
    #Example Query
    cur = conn.cursor()
    cur.execute('SELECT * FROM public."Customer"')
    data = cur.fetchall()
    print(data)
    cur.close()
    return str(data)

if __name__ == '__main__':
    app.run(debug=True)