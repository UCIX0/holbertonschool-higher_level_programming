document.addEventListener('DOMContentLoaded', function() {
    function translateHello() {
        var languageCode = document.getElementById('language_code').value;
        
        if (languageCode === '') {
            alert('Por favor, elige un idioma.');
            return;
        }

        fetch(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`)
            .then(function(response) {
                if (!response.ok) {
                    throw new Error('La respuesta de la red no fue ok');
                }
                return response.json();
            })
            .then(function(data) {
                document.getElementById('hello').textContent = data.hello;
            })
            .catch(function(error) {
                console.error('Hubo un problema con la operación fetch:', error);
            });
    }

    // Añade un evento click al botón "Translate"
    var translateButton = document.getElementById('btn_translate');
    translateButton.addEventListener('click', translateHello);
});
