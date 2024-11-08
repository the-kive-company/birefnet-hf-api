from flask import Blueprint, request, jsonify, send_file, current_app
from werkzeug.utils import secure_filename
import os
from app.services.image_processor import ImageProcessor, ProcessingError
from app.middleware.auth import require_api_token

main = Blueprint('main', __name__)
image_processor = ImageProcessor()

@main.route('/process-image', methods=['POST'])
@require_api_token
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the uploaded file
    filename = secure_filename(file.filename)
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    try:
        # Process the image
        saved_paths = image_processor.process_image(
            filepath,
            current_app.config['RESULTS_FOLDER']
        )

        return jsonify({
            'status': 'success',
            'result_files': saved_paths,
            'download_urls': [f'/download/{fname}' for fname in saved_paths]
        })

    except ProcessingError as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Clean up the uploaded file
        if os.path.exists(filepath):
            os.remove(filepath)

@main.route('/download/<filename>')
@require_api_token
def download_file(filename):
    try:
        return send_file(
            os.path.join(current_app.config['RESULTS_FOLDER'], filename),
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@main.route('/token', methods=['GET'])
def get_token():
    """Endpoint to retrieve the current API token - for development only"""
    if current_app.config['ENV'] == 'development':
        return jsonify({'token': current_app.config['API_TOKEN']})
    return jsonify({'error': 'Not available in production'}), 403
