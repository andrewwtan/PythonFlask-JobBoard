from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/jobs")
def jobs():
    return render_template('index.html')

# above run with 'FLASK_APP=app.py flask run'

# if __name__=="__main__": 
#     app.run(debug='False')

# above run with 'python app.py'