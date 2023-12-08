# Importation des modules nécessaires
from flask import Flask, render_template, request, jsonify, url_for
from PIL import Image
import requests
from io import BytesIO
import sys
import urllib.request
import ffmpeg
import datetime


# Initialisation de l'application Flask
app = Flask(__name__)


# Définition de la route principale pour afficher la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')


# Définition de la route pour le traitement d'image et de vidéo (POST)
@app.route('/compress', methods=['POST'])
def compress():
    # Récupération de l'URL de l'image ou de la vidéo à compresser depuis le formulaire
    input_url = request.form.get('input_url')

    # Vérification de la présence de l'URL
    if not input_url:
        return jsonify({'error': 'Please provide an image or video URL.'}), 400

    # Vérification du type de ressource (image ou vidéo)
    if input_url.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # Traitement de l'image
        return compress_image(input_url)
    elif input_url.lower().endswith(('.mp4', '.avi', '.webm', '.mkv')):
        # Traitement de la vidéo
        return compress_video(input_url)
    else:
        return jsonify({'error': 'Unsupported file format.'}), 400


# Fonction pour effectuer la compression de l'image
def compress_image(input_url):
    # Tentative de téléchargement du contenu depuis l'URL fournie
    try:
        response = requests.get(input_url)
        response.raise_for_status()
    except requests.RequestException as e:
        return jsonify({'error': f'Failed to download content from the provided URL. {str(e)}'}), 400

    # Tentative de compression du contenu téléchargé
    try:
        compressed_resource = compress_resource(response.content)
        return jsonify(compressed_resource)
    except Exception as e:
        return jsonify({'error': f'Failed to compress the image. {str(e)}'}), 500


# Fonction pour effectuer la compression de la vidéo
def compress_video(input_url):
    try:
        urllib.request.urlretrieve(input_url, 'video.mp4')
        compressed_video_info = compress_video_file()
        return jsonify(compressed_video_info), 200
    except Exception as e:
        # En cas d'échec, retourne simplement l'URL de la vidéo compressée sans les détails
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        out_filename = f'compressed_video_{timestamp}.mp4'
        compressed_video_info = compress_video_file()
        return jsonify(compressed_video_info), 200


# Fonction pour compresser la vidéo et récupérer les informations
def compress_video_file():
    in_filename = 'video.mp4'
    # Ajout de l'horodatage au nom du fichier de sortie
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    out_filename = f'compressed_video_{timestamp}.mp4'

    try:
        (
            ffmpeg.input(in_filename)
            .output(out_filename)
            .run()
        )
        with open(out_filename, 'rb') as f:
            lines = f.read()
        with open(f'static/{out_filename}', 'wb') as output_file:
            output_file.write(lines)
        # Génération de l'URL pour l'image compressée
        output_url = url_for('static', filename=out_filename)
        # Utilisation de ffmpeg.probe pour obtenir des informations sur la vidéo compressée
        probe = ffmpeg.probe(out_filename)
        # Affichage des informations dans la console
        print(probe)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)

        width = int(video_stream['width'])
        height = int(video_stream['height'])
        codec_long_name = str(video_stream['codec_long_name'])
        # Retourne les informations sur la vidéo compressée
        compressed_video_info = {
            'output_url': output_url,
            'input_size': 'n/a',  # Conversion en Ko
            'output_size': 'n/a',  # Conversion en Ko
            'input_dimensions': 'n/a',
            'output_dimensions': {'width': width, 'height': height},
            'input_format': 'video',
            'output_format': codec_long_name
        }

        return compressed_video_info

    except ffmpeg.Error as e:
        print(e.stderr.decode(), file=sys.stderr)
        sys.exit(1)


# Fonction pour effectuer la compression de l'image
def compress_resource(content):
    # Tentative d'ouverture de l'image à partir du contenu binaire
    try:
        img = Image.open(BytesIO(content))
    except Exception as e:
        return {'error': f'Failed to process the image. {str(e)}'}

    # Application de la logique de compression réelle
    resized_img = img.resize((int(img.width / 2), int(img.height / 2)))

    # Création d'un tampon pour stocker l'image compressée
    compressed_buffer = BytesIO()
    resized_img.save(compressed_buffer, format='WebP')
    compressed_content = compressed_buffer.getvalue()

    # Choix d'un nom de fichier pour l'image compressée
    output_filename = 'compressed_image.webp'

    # Sauvegarde du fichier compressé dans le dossier statique
    with open(f'static/{output_filename}', 'wb') as output_file:
        output_file.write(compressed_content)

    # Génération de l'URL pour l'image compressée
    output_url = url_for('static', filename=output_filename)

    # Création d'un objet contenant les informations sur la compression
    compressed_resource = {
        'output_url': output_url,
        'input_size': len(content) // 1024,  # Conversion en Ko
        'output_size': len(compressed_content) // 1024,  # Conversion en Ko
        'input_dimensions': {'width': img.width, 'height': img.height},
        'output_dimensions': {'width': resized_img.width, 'height': resized_img.height},
        'input_format': 'image',
        'output_format': 'webp'
    }
    return compressed_resource


# Point d'entrée pour exécuter l'application Flask en mode débogage
if __name__ == '__main__':
    app.run(debug=True)
