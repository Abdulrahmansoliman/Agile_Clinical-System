from flask import Flask,redirect,url_for,render_template,request, jsonify
import requests
from models.init import *
from flask_cors import CORS

#-------------APP CONFIGURATION----------------#

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=  'sqlite:///data.db'
app.config['secret_key']='secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app, origins="*", methods=["GET", "POST", "PUT", "DELETE"], allow_headers="*")

with app.app_context():
    db.init_app(app)
    


#-------------BluePrints-----------------------#

with app.app_context():
    from routes.doctors.views import doctors_blueprint
    from routes.clinicitems.views import clinicitems_blueprint
    app.register_blueprint(doctors_blueprint, url_prefix='/doctors')
    app.register_blueprint(clinicitems_blueprint, url_prefix='/clinicitems')
#-----------------------------------------------#

# this endpoint avoids errors that arise when the database
# in concurrently created by multiple gunicorn workers in build
# time and it should be removed in production

@app.route('/init')
def init():
    db.engine.execute(
        "SELECT 'drop table ' || name || ';' FROM sqlite_master WHERE type = 'table';").fetchall()
    import db_initialization_script
    db.create_all(app=app)

    return jsonify({
        'success': True
    }), 200


@app.route('/')
def index():

    db.create_all(app=app)
    import db_initialization_script
    doctors = Doctor.query.all()
    secretaries = Secretary.query.all()

    return jsonify({
            'data': [d.format() for d in doctors] + [s.format() for s in secretaries]
    }), 200

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
    

