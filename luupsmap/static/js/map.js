const VIENNA_COORDS = {
  lat: 48.208176,
  lng: 16.373819
};

const DEFAULT_ZOOM = 15;

let map;  // the map object

// FUNCTIONS ///////////////////////////////////////////////////////////////////////////////////////////////////////////

getMapContainer = () => document.getElementById('map');

initMap = () => {
  const options = {
    center: VIENNA_COORDS,
    zoom: DEFAULT_ZOOM
  };
  map = new google.maps.Map(getMapContainer(), options);
  const marker = new google.maps.Marker({
    map,
    position: VIENNA_COORDS,
    title: 'Wien!',
    animation: google.maps.Animation.DROP
  });
};
