from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Database connection settings
DB_HOST = "localhost"
DB_NAME = "myresume"
DB_USER = "postgres"
DB_PASSWORD = "8106"

# Function to connect to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')  # Resume page

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']

    # Connect to PostgreSQL
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert into table (make sure table 'messages' exists)
    cursor.execute('''
        INSERT INTO messages (name, message)
        VALUES (%s, %s)
    ''', (name, message))

    # Save changes and close connection
    conn.commit()
    cursor.close()
    conn.close()

    # Return confirmation
    return f"<h1>Thank you, {name}!</h1><p>Your message: {message}</p>"

if __name__ == '__main__':
    app.run(debug=True)
