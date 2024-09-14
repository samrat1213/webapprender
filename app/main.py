from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)

# List of shady quotes
quotes = [
    "Not everything is as it seems.",
    "Secrets have a cost; they’re not for free.",
    "Trust is a dangerous game.",
    "Nothing personal, it's just business.",
    "Beware of the quiet ones.",
    "Truth is rarely pure and never simple.",
    "Some things are better left in the dark."
]

@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    quote = random.choice(quotes)  # Select a random shady quote
    return render_template('index.html', time=current_time, quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
