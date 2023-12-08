# Image and Video Compression API

This is a simple Flask-based web application for compressing images and videos. The application allows users to provide the URL of an image or video, and it returns the compressed version along with relevant information such as input/output size, dimensions, and format.

## Getting Started

### Prerequisites
Make sure you have Python and the required dependencies installed. You can install them using the following command:
pip install -r requirements.txt
Running the Application
Run the app.py script to start the Flask application. Open a web browser and navigate to http://localhost:5000 to access the application.
```bash
python app.py
### Usage
Access the web interface by visiting http://localhost:5000 in your browser.
Enter the URL of the image or video you want to compress.
Click the "Compress" button.
View the compression results, including input/output size, dimensions, format, and the URL of the compressed media.
### File Structure
app.py: The main Flask application script.
static/: Directory containing static files (CSS, JS).
templates/: HTML templates used by the application.
### Technologies Used
Flask: Micro web framework for Python.
Bootstrap: Front-end framework for responsive design.
Pillow: Python Imaging Library for image processing.
FFmpeg: Multimedia framework for video processing.
### Contributors
Chebbi Abir
### Acknowledgments
Thanks to the developers of Flask, Bootstrap, Pillow, and FFmpeg for their excellent tools.
Feel free to update the sections as needed, including adding your name to the contributors and providing a proper license file (if applicable).
