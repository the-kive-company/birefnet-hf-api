import os
from secrets import token_hex

class Config:
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'instance/uploads')
    RESULTS_FOLDER = os.getenv('RESULTS_FOLDER', 'instance/results')
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', 16 * 1024 * 1024))  # 16MB max file size

    # Generate a random token if not provided through environment
    API_TOKEN = os.getenv('API_TOKEN', token_hex(32))
