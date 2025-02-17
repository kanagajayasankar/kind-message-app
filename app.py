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

# List of dynamic background images
background_images = [
    "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
    "https://images.unsplash.com/photo-1533612608997-212b06408fdf?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
    "https://images.unsplash.com/photo-1495954380655-01609180fc2d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
    "https://images.unsplash.com/photo-1542140461-1c5f00b289f4?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
   
