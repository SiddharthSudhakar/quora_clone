from tempfile import gettempdir # Handling temporary files
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask_session import Session # Handle sessions
from flask_cli import FlaskCLI # Run commandline scripts - for initdb()
import config
import os # For getting environment variables

app = Flask(__name__)

app.config.from_object('config.Development') # Load config # TODO-deployment replace with 'Production'
FlaskCLI(app) # Pass context to Flask CLI app
mongo = PyMongo(app) # Pass context to PyMongo

# configure session to use filesystem (instead of signed cookies)
app.config['SESSION_FILE_DIR']  = gettempdir()
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE']      = 'filesystem'
Session(app)


@app.cli.command()
def initdb():
    # print ("INIT",os.environ.get("MYSQL_PASSWORD"))
    # """Initializes the database."""
    # db = mysql.connection.cursor()
    # with app.open_resource('SQL/incubate.sql', mode='r') as f:
    #     db.execute(f.read())
    # print('Initialized the database.')

@app.route('/posts', methods=['GET'])
def get_all_posts():
    posts = mongo.db.posts
    output = []
    for p in posts.find():
        output.append({'title': posts['title'],
                       'description': posts['description'],
                       'posted_by': posts['by'],
                       'likes': posts['likes'],
                       'dislikes': posts['dislikes'],
                       'resolved': posts['resolved'],
                       'answers': posts['answers']
                       })
    return jsonify({'result': output})



if __name__ == '__main__':
    app.run()