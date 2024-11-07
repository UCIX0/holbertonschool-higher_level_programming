const numberTitle = document.querySelector('#list_movies')
const url = 'https://swapi-api.hbtn.io/api/films/?format=json'

fetch(url)
    .then(res => res.json())
    .then(function(data){
        const movies = data.results;
              movies.forEach((movie) => {
                const movieTitle = movie.title;
                const listItem = document.createElement('li')
                listItem.textContent = movieTitle
                numberTitle.appendChild(listItem)
              })
    })
    .catch(error => console.log(error))