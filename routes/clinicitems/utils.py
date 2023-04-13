from flask import abort, jsonify

def validate_clinicitem_id(clinicitem_id):
    if clinicitem_id is None:
        abort(400, 'No clinicitem with the id provided')
    
    return jsonify({
        'success': True,
    })