# import os

# # Heroku check
# is_heroku = False
# if 'IS_HEROKU' in os.environ:
#     is_heroku = True

# Flask
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
 
# Initialize Flask application
app = Flask(__name__)

# Set up your default route
@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/industry')
def industry():
    return render_template('industry.html')

@app.route('/stockanalysis')
def stock_analysis():
    return render_template('stock_analysis.html')

if __name__ == "__main__":
    app.run(debug=True)