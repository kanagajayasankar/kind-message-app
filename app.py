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
    # Load messages and select one
    messages = load_messages()
    message = random.choice(messages)
    
    # Static background image URL
    background_image = "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080"
    
    # HTML template with the menu bar and styled content
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
                color: #ffffff;
                background-color: #1a1a1a; /* Fallback color */
                background-image: url('{background_image}');
                background-size: cover;
                background-position: center;
                overflow: hidden;
            }}

            /* Side Top Menu Bar */
            .menu {{
                position: absolute;
                top: 20px;
                left: 20px;
                display: flex;
                flex-direction: column;
                gap: 10px;
            }}

            .menu a {{
                color: #ffffff;
                text-decoration: none;
                font-size: 1.2rem;
                font-weight: bold;
                padding: 0.5rem 1rem;
                background-color: rgba(0, 0, 0, 0.6);
                border-radius: 10px;
                transition: background-color 0.3s ease;
            }}

            .menu a:hover {{
                background-color: rgba(255, 255, 255, 0.3);
            }}

            /* Styling for the random message */
            .message {{
                position: absolute;
                top
