const apiKey = '003a04db4db142f479fa9aa76d92df10';
const apiUrl1 ='https://api.openweathermap.org/data/2.5/weather?'

const myURLonVercel 'https://weatherpython.vercel.app/'

const locationInput = document.getElementById('locationInput');
const searchButton = document.getElementById('searchButton');
const locationElement = document.getElementById('location');
const temperatureElement = document.getElementById('temperature');
const descriptionElement = document.getElementById('description');
const weatherNowElement = document.getElementById('weathernow');
const backgroundImages = [
    'test.png',
    'test2.jpg',
    'test3.jpg',
    'test4.webp',
    'test5.webp',
    'test6.webp',
    'test7.jpg'
    // Add more image names as needed
];

function setRandomBackground() {
    // Generate a random index within the range of the backgroundImages array
    const randomIndex = Math.floor(Math.random() * backgroundImages.length);

    // Get the randomly selected image file name
    const selectedImage = backgroundImages[randomIndex];
console.error(selectedImage);
    // Update the background image of the body element
    document.body.style.backgroundImage = `url('${selectedImage}')`;
}

searchButton.addEventListener('click', () => {
    const location = locationInput.value;
    if (location) {
       // console.error("SomethingWrong");
        fetchWeather(location);
    
    }
    else{
        locationElement.textContent = "Please input a location";
    }
});

function fetchWeather(location) {
    /*const url = `${apiUrl}?id=524901&q=${location}&appid=${apiKey}&units=metric`; */
    // const url = `${apiUrl1}q=${location}&appid=${apiKey}&units=metric`;
    const urlPython = '${myURLonVercel}'

    fetch(urlPython)
        .then(response => response.json())
        .then(data => {
            setRandomBackground();  
            locationElement.textContent = data;         
           /* 
           locationElement.textContent = data.name;
            temperatureElement.textContent = `${Math.round(data.main.temp)}°C`;
            descriptionElement.textContent = data.weather[0].main;
            try {
            weatherNowElement.textContent = data.weather[1].main;
                
            } catch (error) { 
                
            } */
        })
        .catch(error => {
            locationElement.textContent = "No Data Returned, Check Your Location";
            console.error('Error fetching weather data:', error);
              temperatureElement.textContent = "";
            descriptionElement.textContent = "";
            
            weatherNowElement.textContent = "";
                
           
        });
}