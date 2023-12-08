# Image and Video Compression API

This is a simple Flask-based web application for compressing images and videos. The application allows users to provide the URL of an image or video, and it returns the compressed version along with relevant information such as input/output size, dimensions, and format.

## Getting Started

### Prerequisites
Make sure you have Python and the required dependencies installed. You can install them using the following command:
pip install -r requirements.txt
Running the Application
Run the app.py script to start the Flask application. Open a web browser and navigate to http://localhost:5000 to access the application.
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

### About FFmpeg
FFmpeg is the leading multimedia framework, able to decode, encode, transcode, mux, demux, stream, filter and play pretty much anything that humans and machines have created. It supports the most obscure ancient formats up to the cutting edge. No matter if they were designed by some standards committee, the community or a corporation. It is also highly portable: FFmpeg compiles, runs, and passes our testing infrastructure FATE across Linux, Mac OS X, Microsoft Windows, the BSDs, Solaris, etc. under a wide variety of build environments, machine architectures, and configurations.
### Étapes pour installer FFmpeg sur Windows :
## Téléchargement de l'Exécutable FFmpeg :

Rendez-vous sur la page de téléchargement de FFmpeg.
Sous "Windows Builds," vous pouvez sélectionner un lien pour télécharger l'exécutable statique ou partagé.
Choisissez l'option qui correspond le mieux à vos besoins. L'exécutable statique est plus simple à utiliser.
## Extraction de l'Archive :

Une fois le téléchargement terminé, extrayez le contenu de l'archive ZIP dans un dossier de votre choix. Vous pouvez utiliser un outil comme 7-Zip ou l'extracteur de fichiers Windows intégré.
## Déplacement de FFmpeg :

Déplacez le dossier extrait (contenant les fichiers ffmpeg.exe, ffprobe.exe, etc.) dans un emplacement permanent sur votre disque dur, par exemple, C:\ffmpeg.
### Étapes pour configurer les variables d'environnement :
## Ouverture du Panneau de Configuration :

Cliquez avec le bouton droit sur "Ce PC" ou "Ordinateur" sur votre bureau ou dans l'Explorateur de fichiers.
Sélectionnez "Propriétés."
## Accès aux Paramètres Système Avancés :

Cliquez sur "Paramètres système avancés" dans le volet de gauche.
## Ouverture de la Fenêtre des Variables d'Environnement :

Dans la fenêtre Système, cliquez sur le bouton "Variables d'environnement..."
## Modification de la Variable PATH :

Dans la section "Variables système," sélectionnez la variable "Path" et cliquez sur "Modifier..."
## Ajout du Chemin de FFmpeg :

Cliquez sur "Nouveau" et ajoutez le chemin complet du dossier où vous avez extrait FFmpeg (par exemple, C:\ffmpeg).
Cliquez sur "OK" pour fermer toutes les fenêtres.
## Vérification de l'Installation :

Ouvrez une nouvelle fenêtre de commande (cmd) et tapez les commandes suivantes pour vérifier que FFmpeg est bien installé :

ffmpeg -version
ffprobe -version


Vous devriez voir les informations de version pour FFmpeg et FFprobe s'afficher dans la console.

Maintenant, FFmpeg est installé sur votre système Windows et est configuré dans les variables d'environnement, ce qui signifie que vous pouvez l'utiliser depuis n'importe quel répertoire dans la ligne de commande.


