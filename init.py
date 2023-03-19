from flask import Flask,redirect,url_for,render_template,request, jsonify
from models.models  import *
import models.models as models
import db_initialization_script

#-------------APP CONFIGURATION----------------#

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['secret_key']='secret_key'

#-----------------------------------------------#


@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

# this endpoint avoids errors that arise when the database
# in concurrently created by multiple gunicorn workers in build
# time and it should be removed in production

@app.route('/init')
def init():
    db.engine.execute("DROP SCHEMA public CASCADE;")
    db.engine.execute("CREATE SCHEMA public;")

    db.create_all(app=app)

    return jsonify({
        'success': True
    }), 200


@app.route('/')
def index():
    
    data = models.query.all()
    
    return jsonify({
     data.json()   
    }), 200

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
    
    