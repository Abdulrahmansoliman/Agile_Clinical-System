from flask import abort, jsonify

def validate_doctor_id(doctor_id):
    if doctor_id is None:
        abort(400, 'No doctor with the id provided')
    
    return jsonify({
        'success': True,
    })

