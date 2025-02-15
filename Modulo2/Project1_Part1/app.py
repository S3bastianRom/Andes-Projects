# Import the Flask library
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page ("/")
@app.route('/')
def home():
    return "Hello, Flask!"  # Return a simple message

# Define a route for the "/about" page
@app.route('/about')
def about():
    return "This is a simple Flask app!"

# Run the application (only if the script is run directly)
if __name__ == '__main__':
    app.run(debug=True)