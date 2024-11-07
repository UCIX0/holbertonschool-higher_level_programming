const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

fetch(url)
    .then(res => res.json())
    .then(function(data){
        hello.textContent = data.hello;
    })
    .catch(error => console.log(error))