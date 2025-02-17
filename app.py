from flask import Flask, render_template_string
import random

app = Flask(__name__)

# Load messages from a file
def load_messages():
    try:
        with open('messages.txt', 'r', encoding='utf-8') as file:
            # Strip whitespace and exclude empty lines
            messages = [line.strip() for line in file if line.strip()]
        return messages
    except FileNotFoundError:
        return ["Oops! No messages found. Please add a 'messages.txt' file."]

# List of dynamic background images
background_images = [
    "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
    "https://images.unsplash.com/photo-1533612608997-212b06408fdf?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
    "https://images.unsplash.com/photo-1495954380655-01609180fc2d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
    "https://images.unsplash.com/photo-1542140461-1c5f00b289f4?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
    "https://images.unsplash.com/photo-1517832606290-98c3f00664a6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080"
]

@app.route('/')
def home():
    # Load messages and select one
    messages = load_messages()
    message = random.choice(messages)
    
    # Select a random background image
    background_image = random.choice(background_images)
    
    # HTML template with dynamic background and content
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
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                color: #ffffff;
                text-align: center;
                background-color: #1a1a1a; /* Fallback color */
                background-image: url('{background_image}');
                background-size: cover;
                background-position: center;
                overflow: hidden;
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

            /* Styling for the Instagram link */
            .insta-link {{
                color: #FFD700; /* Gold color */
                text-decoration: none;
                font-weight: bold;
                font-size: 1.5rem;
                margin-top: 1.5rem;
                padding: 0.5rem 1rem;
                background-color: rgba(0, 0, 0, 0.5);
                border-radius: 10px;
                transition: transform 0.3s ease, background-color 0.3s ease;
            }}

            .insta-link:hover {{
                background-color: rgba(255, 223, 0, 0.8);
                transform: scale(1.05);
            }}

            /* Refresh link styling */
            .link {{
                font-size: 1.2rem;
                color: #ffb6c1;
                text-decoration: none;
                background-color: rgba(255, 255, 255, 0.1);
                padding: 0.5rem 1rem;
                border-radius: 8px;
                transition: all 0.3s ease;
                margin-top: 1rem;
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
        <a href="https://www.instagram.com/light_beyond_shadows?igsh=MWx1NjNrdGQ1bDY1ZQ%3D%3D&utm_source=qr" 
           class="insta-link" target="_blank">
            Check out my Instagram: light_beyond_shadows
        </a>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(debug=True)
