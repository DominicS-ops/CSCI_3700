from flask import Flask, render_template, jsonify
import util

# Initialize the Flask app
app = Flask(__name__)

# Database connection parameters
username = 'raywu1990'
password = 'test'
host = '127.0.0.1'
port = '5432'
database = 'dvdrental'

# Route to insert (5, 'Cherry') into basket_a
@app.route('/api/update_basket_a')
def update_basket_a():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    
    try:
        cursor.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry')")
        connection.commit()
        message = "Success!"
    except Exception as error:
        connection.rollback()
        message = f"Error: {error}"
    
    util.disconnect_from_db(connection, cursor)
    return message

# Route to display unique fruits from both baskets
@app.route('/api/unique')
def show_unique_fruits():
    cursor, connection = util.connect_to_db(username, password, host, port, database)

    try:
        # Query to get unique fruits from basket_a (not in basket_b)
        cursor.execute("""
            SELECT fruit_a 
            FROM basket_a 
            LEFT JOIN basket_b ON basket_a.fruit_a = basket_b.fruit_b 
            WHERE basket_b.fruit_b IS NULL
        """)
        unique_a = [row[0] for row in cursor.fetchall()]

        # Query to get unique fruits from basket_b (not in basket_a)
        cursor.execute("""
            SELECT fruit_b 
            FROM basket_b 
            LEFT JOIN basket_a ON basket_b.fruit_b = basket_a.fruit_a 
            WHERE basket_a.fruit_a IS NULL
        """)
        unique_b = [row[0] for row in cursor.fetchall()]

        util.disconnect_from_db(connection, cursor)

        # Render the template with the unique fruits
        return render_template('index.html', unique_a=unique_a, unique_b=unique_b)

    except Exception as error:
        util.disconnect_from_db(connection, cursor)
        return f"Error: {error}"

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1')

