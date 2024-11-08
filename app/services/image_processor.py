from gradio_client import Client, handle_file
import os
import shutil

class ImageProcessor:
    def __init__(self):
        self.client = Client("ZhengPeng7/BiRefNet_demo")

    def process_image(self, input_path, results_folder):
        try:
            # Process the image with BiRefNet
            result_paths = self.client.predict(
                images=handle_file(input_path),
                resolution="Hello!!",
                weights_file="General",
                api_name="/image"
            )

            # Copy results to our results folder with meaningful names
            saved_paths = []
            filename = os.path.basename(input_path)
            for i, temp_path in enumerate(result_paths):
                ext = os.path.splitext(temp_path)[1]
                result_filename = f"{os.path.splitext(filename)[0]}_result_{i}{ext}"
                result_path = os.path.join(results_folder, result_filename)
                shutil.copy2(temp_path, result_path)
                saved_paths.append(result_filename)

            return saved_paths

        except Exception as e:
            raise ProcessingError(f"Error processing image: {str(e)}")

class ProcessingError(Exception):
    pass
