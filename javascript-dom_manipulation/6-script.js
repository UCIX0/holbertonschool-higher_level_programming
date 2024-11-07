const character = document.querySelector('#character')
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json'
fetch(url)
    .then(response => response.json())
    .then(function(data){
        const name = data.name
        character.textContent = name;
    })
    .catch(error => console.log(error))
