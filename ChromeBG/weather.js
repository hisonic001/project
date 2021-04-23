const weather = document.querySelector(".js-weather");

const API_key = 'd7ba80bb279cf0a0a99d9fe764d354f1';
const COORDS = 'coords';

function getWeather(lat, lon){
    fetch(`http://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_key}&units=metric`
    ).then(function(res){
        return res.json()
    }).then(function(json){
        const temperature = json.main.temp;
        const place = json.name;
        console.log(json);
        weather.innerHTML = `${temperature}℃ @ ${place}`
    })

}

function saveCoords(coordsObj){
    localStorage.setItem(COORDS,JSON.stringify(coordsObj));
}

function handleGeoSucces(position){
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    const coordsObj = {
        latitude, longitude
    };
    saveCoords(coordsObj);
    getWeather(latitude,longitude);
}

function handleGeoError(){
    console.log("cant get geo location");
}

function askForCoords(){
    navigator.geolocation.getCurrentPosition(handleGeoSucces, handleGeoError);
}

function loadCoords(){
    const loadedCoords = localStorage.getItem(COORDS);
        if(loadedCoords === null){
            askForCoords();
        }
        else{
            const parsedCoords = JSON.parse(loadedCoords);
            getWeather(parsedCoords.latitude,parsedCoords.longitude);
        }

}


function init(){
    loadCoords();
}

init();
