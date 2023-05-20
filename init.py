from flask import Flask, redirect, url_for, render_template, request, jsonify
import requests
from models.init import *
from flask_cors import CORS

# -------------APP CONFIGURATION----------------#

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['secret_key'] = 'secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app, origins="*", methods=["GET", "POST",
     "PUT", "DELETE", "PATCH"], allow_headers="*")

with app.app_context():
    db.init_app(app)


# -------------BluePrints-----------------------#

with app.app_context():
    from routes.doctors.views import doctors_blueprint
    from routes.clinicitems.views import clinicitems_blueprint
    from routes.sercretaries.views import secretaries_blueprint
    from routes.patients.views import patients_blueprint
    from routes.appointments.views import appointments_blueprint
    from routes.records.views import records_blueprint
    from routes.auth.views import auth_blueprint

    app.register_blueprint(secretaries_blueprint, url_prefix='/secretaries')
    app.register_blueprint(doctors_blueprint, url_prefix='/doctors')
    app.register_blueprint(clinicitems_blueprint, url_prefix='/clinicitems')
    app.register_blueprint(patients_blueprint, url_prefix='/patients')
    app.register_blueprint(appointments_blueprint, url_prefix='/appointments')
    app.register_blueprint(records_blueprint, url_prefix='/records')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
# -----------------------------------------------#

# this endpoint avoids errors that arise when the database
# in concurrently created by multiple gunicorn workers in build
# time and it should be removed in production


@app.route('/init')
def init():

    db.drop_all()

    try:
        db.engine.execute(
            "SELECT 'drop table ' || name || ';' FROM sqlite_master WHERE type = 'table';").fetchall()
    except:
        pass
    db.create_all()
    import db_initialization_script

    return jsonify({
        'success': True
    }), 200


@app.route('/')
def index():

    doctors = Doctor.query.all()
    secretaries = Secretary.query.all()

    return jsonify({
        'data': [d.format() for d in doctors] + [s.format() for s in secretaries]
    }), 200


if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True)
