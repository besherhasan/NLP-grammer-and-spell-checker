# Import necessary libraries and modules
from flask import Flask, render_template, request
from language_tool_python import LanguageTool

# Create a Flask application instance
app = Flask(__name__)

# Create a LanguageTool object for grammar and spell checking
tool = LanguageTool('en-US')

# Define a route for the root URL ('/') that renders an HTML template
@app.route('/')
def index():
    return render_template('index.html', corrected_text='')

# Define a route for the '/spell' URL that handles POST requests
@app.route('/spell', methods=['POST'])
def spell_check():
    text = request.form['text']

    # Perform spell and grammar checking using LanguageTool
    errors = tool.check(text)

    # Generate corrected text with spelling and grammar suggestions
    corrected_text = tool.correct(text)

    return render_template('index.html', corrected_text=corrected_text)

# Run the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
