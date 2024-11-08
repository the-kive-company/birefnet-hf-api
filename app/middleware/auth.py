from functools import wraps
from flask import request, jsonify, current_app

def require_api_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return jsonify({'error': 'No Authorization header'}), 401

        try:
            # Expected format: "Bearer <token>"
            scheme, token = auth_header.split()
            if scheme.lower() != 'bearer':
                return jsonify({'error': 'Invalid authentication scheme'}), 401

            if token != current_app.config['API_TOKEN']:
                return jsonify({'error': 'Invalid token'}), 401

        except ValueError:
            return jsonify({'error': 'Invalid Authorization header format'}), 401

        return f(*args, **kwargs)
    return decorated_function
