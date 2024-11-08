# Image Processing API with BiRefNet

A Flask-based REST API that processes images using the BiRefNet model via the Gradio client, with Docker support and token-based authentication.

## Features

- Image processing using the BiRefNet model through Gradio client
- RESTful API endpoints
- Token-based authentication middleware
- Docker and Docker Compose support
- Organized project structure
- File upload and download capabilities
- Configuration via environment variables
- Dependency management with Poetry
- Supports both local development and containerized deployment

## Prerequisites

- Python 3.10 or higher
- Docker and Docker Compose (for containerized deployment)
- Poetry (for local development)

## Project Structure

```
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── routes.py
│   ├── middleware
│   │   └── auth.py
│   └── services
│       └── image_processor.py
├── instance
│   ├── uploads
│   └── results
├── run.py
├── pyproject.toml
├── poetry.lock
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── README.md
```

## Installation

### Local Development

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install dependencies with Poetry:**

   Ensure you have [Poetry](https://python-poetry.org/docs/#installation) installed.

   ```bash
   poetry install
   ```

3. **Run the application:**

   ```bash
   poetry run python run.py
   ```

   The application will be accessible at `http://0.0.0.0:6000`.

### Docker Deployment

1. **Build and run the Docker container:**

   ```bash
   docker-compose up --build
   ```

2. **Access the application:**

   The application will be accessible at `http://0.0.0.0:6000`.

## Usage

### Authentication

All endpoints require an API token for authentication.

- **Environment Variable:**

  Set the `API_TOKEN` environment variable to your desired token. If not set, a token will be randomly generated.

- **Providing the Token:**

  Include the token in the `Authorization` header of your requests using the Bearer scheme:

  ```
  Authorization: Bearer YOUR_API_TOKEN
  ```

### API Endpoints

#### `POST /process-image`

Process an image using the BiRefNet model.

- **Headers:**
  - `Authorization: Bearer YOUR_API_TOKEN`

- **Form Data:**
  - `image`: The image file to be processed.

- **Response:**

  ```json
  {
    "status": "success",
    "result_files": ["original_filename_result_0.ext", "original_filename_result_1.ext"],
    "download_urls": ["/download/original_filename_result_0.ext", "/download/original_filename_result_1.ext"]
  }
  ```

#### `GET /download/<filename>`

Download a processed image file.

- **Headers:**
  - `Authorization: Bearer YOUR_API_TOKEN`

- **Parameters:**
  - `filename`: The name of the file to download.

### Example Request

```bash
curl -X POST http://0.0.0.0:6000/process-image \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -F "image=@/path/to/your/image.jpg"
```

## Configuration

The application can be configured using environment variables:

- `UPLOAD_FOLDER`: Directory for uploaded images (default: `instance/uploads`).
- `RESULTS_FOLDER`: Directory for processed images (default: `instance/results`).
- `MAX_CONTENT_LENGTH`: Maximum upload file size in bytes (default: `16777216` or 16MB).
- `API_TOKEN`: Token used for API authentication (default: randomly generated).

## Dependencies

Main dependencies are specified in `pyproject.toml`:

- `python`: >=3.10,<4.0
- `gradio-client`: ^1.4.0
- `flask`: ^3.0.0

## Notes

- The image processing is performed using the Gradio client to interact with the [BiRefNet_demo](https://huggingface.co/spaces/ZhengPeng7/BiRefNet_demo) hosted on Hugging Face Spaces.
- Ensure you have internet connectivity when running the application, as it requires access to the external model.

## License

[MIT License](LICENSE)

## Acknowledgments

- [BiRefNet](https://github.com/ZhengPeng7/BiRefNet_demo)
- [Gradio](https://gradio.app/)
