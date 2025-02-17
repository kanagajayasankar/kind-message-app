from flask import Flask, render_template_string
import random

app = Flask(__name__)

# Load messages from a file
def load_messages():
    try:
        with open('messages.txt', 'r', encoding='utf-8') as file:
            # Read all lines, stripping whitespace and excluding empty lines
            messages = [line.strip() for line in file if line.strip()]
        return messages
    except FileNotFoundError:
        return ["Oops! No messages found. Please add a 'messages.txt' file."]

@app.route('/')
def home():
    # Load the messages from the file
    messages = load_messages()
    
    # Select a random message
    message = random.choice(messages)
    
    # HTML content for the webpage
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Kind Message</title>
        <style>
            /* Global Reset */
            body, html {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Arial', sans-serif;
                height: 100%;
                overflow: hidden;
            }}

            /* Background styling */
            body {{
                background-image: url('https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080');
                background-size: cover;
                background-position: center;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                color: #ffffff;
                text-align: center;
            }}

            /* Styling for the random message */
            .message {{
                font-size: 2.5rem;
                font-weight: bold;
                background-color: rgba(0, 0, 0, 0.5); /* Adds contrast */
                padding: 1rem 2rem;
                border-radius: 12px;
                margin-bottom: 2rem;
            }}

            /* Styling for the refresh link */
            .link {{
                font-size: 1.2rem;
                color: #ffb6c1;
                text-decoration: none;
                background-color: rgba(255, 255, 255, 0.1);
                padding: 0.5rem 1rem;
                border-radius: 8px;
                transition: all 0.3s ease;
            }}

            .link:hover {{
                background-color: rgba(255, 255, 255, 0.3);
                text-decoration: none;
            }}
        </style>
    </head>
    <body>
        <div class="message">{message}</div>
        <a href="/" class="link">Get Another Message</a>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(debug=True)
