from flask import Flask
import random

# Create the Flask app
app = Flask(__name__)

# List of random messages
messages = ["Hello, world!", "Welcome!", "Have a great day!", "Keep smiling!", "You're awesome!"]

# Define the main route
@app.route('/')
def random_message():
    return random.choice(messages)

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
