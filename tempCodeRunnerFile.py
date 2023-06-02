with app.app_context():
    from routes.doctors.views import doctors_blueprint
    from routes.clinicitems.views import clinicitems_blueprint
    from routes.sercretaries.views import secretaries_blueprint
    from routes.patients.views import patients_blueprint
    from routes.appointments.views import appointments_blueprint
    from routes.records.views import records_blueprint
    from routes.auth.views import auth_blueprint