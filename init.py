from flask import Flask,redirect,url_for,render_template,request, jsonify
import requests
from models.models  import *
import models.models as models


#-------------APP CONFIGURATION----------------#

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=  'sqlite:///data.db'
app.config['secret_key']='secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



with app.app_context():
    db.init_app(app)
    

#-----------------------------------------------#


# this endpoint avoids errors that arise when the database
# in concurrently created by multiple gunicorn workers in build
# time and it should be removed in production

@app.route('/init')
def init():
    with app.app_context():
        db.engine.execute(
            "SELECT 'drop table ' || name || ';' FROM sqlite_master WHERE type = 'table';").fetchall()
        import db_initialization_script
        db.create_all(app=app)

    return jsonify({
        'success': True
    }), 200



@app.route('/')
def index():
    with app.app_context():
        db.create_all(app=app)
        import db_initialization_script
        data = Doctor.query.all()

    return jsonify({
            'data': [d.format() for d in data]
    }), 200

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
    
    