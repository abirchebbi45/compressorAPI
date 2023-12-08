// Fonction pour compresser l'image ou la vidéo
function compressMedia() {
    // Récupérer la valeur de l'URL de l'image ou de la vidéo depuis le champ de saisie
    var inputUrl = document.getElementById("input-url").value;

    // Vérifier si l'URL est vide
    if (!inputUrl) {
        // Afficher une alerte si l'URL est vide
        alert("Please enter an image or video URL.");
        // Sortir de la fonction si l'URL est vide
        return;
    }

    // Créer un objet FormData pour envoyer des données binaires (ici, l'URL de la vidéo) via une requête POST
    var formData = new FormData();
    formData.append("input_url", inputUrl);

    // Effectuer une requête fetch vers l'endpoint "/compress" avec la méthode POST et les données FormData
    fetch("/compress", {
        method: "POST",
        body: formData
    })
        // Traiter la réponse de la requête
        .then(response => {
            // Vérifier si la réponse indique une erreur HTTP
            if (!response.ok) {
                // Lancer une erreur avec le statut HTTP si la réponse n'est pas OK
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            // Retourner la réponse sous forme JSON
            return response.json();
        })
        // Traiter les données JSON de la réponse
        .then(data => {
            // Vérifier s'il y a une erreur dans les données
            if (data.error) {
                // Afficher une alerte avec le message d'erreur si une erreur est présente
                alert(`Failed to compress the image or video. ${data.error}`);
            } else {
                // Afficher les informations de compression si aucune erreur n'est présente
                displayCompressionInfo(data);
            }
        })
        // Gérer les erreurs potentielles lors de la requête ou du traitement des données
        .catch(error => {
            // Afficher l'erreur dans la console
            console.error("Error:", error);
            // Afficher une alerte générique en cas d'échec de la compression
            alert("Failed to compress the image or video. Please try again.");
        });
}

// Fonction pour afficher les informations de compression dans l'interface utilisateur
function displayCompressionInfo(data) {
    // Vérifier si les propriétés nécessaires existent dans les données
    if (!data || !data.input_size || !data.output_size || !data.input_dimensions || !data.output_dimensions || !data.input_format || !data.output_format || !data.output_url) {
        // Afficher une alerte en cas de données manquantes
        alert("Failed to get compression information. Please try again.");
        return;
    }

    // Mettre à jour les éléments HTML avec les informations de compression
    document.getElementById("input-size").innerText = data.input_size + " KB";
    document.getElementById("output-size").innerText = data.output_size + " KB";

    // Vérifier si les dimensions d'entrée et de sortie existent
    if (data.input_dimensions && data.input_dimensions.width && data.input_dimensions.height) {
        document.getElementById("input-dimensions").innerText = `${data.input_dimensions.width} x ${data.input_dimensions.height}`;
    }

    if (data.output_dimensions && data.output_dimensions.width && data.output_dimensions.height) {
        document.getElementById("output-dimensions").innerText = `${data.output_dimensions.width} x ${data.output_dimensions.height}`;
    }

    // Vérifier si les formats d'entrée et de sortie existent
    if (data.input_format) {
        document.getElementById("input-format").innerText = data.input_format;
    }

    if (data.output_format) {
        document.getElementById("output-format").innerText = data.output_format;
    }

    // Mettre à jour le lien et le texte de l'URL de sortie
    document.getElementById("output-url").innerText = "Output URL: " + data.output_url;
    document.getElementById("output-url").href = data.output_url;

    // Afficher le bloc d'informations de sortie
    document.getElementById("output-info").style.display = "block";
}
