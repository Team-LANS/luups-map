const VENUE_TYPES = {
  RESTAURANT: 'RESTAURANT',
  BAR: 'BAR',
  VENUE: 'VENUE'
};

const VIENNA_COORDS = {
  lat: 48.208176,
  lng: 16.373819
};

const DEFAULT_ZOOM = 15;

let map;  // the map object

// FUNCTIONS ///////////////////////////////////////////////////////////////////////////////////////////////////////////

getMapContainer = () => document.getElementById('map');

getMarkerIcon = (type) => {
  return {
    url: `${location.href}static/svg/marker/${VENUE_TYPES[type]}.svg`,
    scaledSize: new google.maps.Size(45, 45)
  }
};

addMarker = (type, position) => {
  return new google.maps.Marker({
    map,
    position,
    animation: google.maps.Animation.DROP,
    icon: getMarkerIcon(type)
  });
};

initMap = () => {
  const options = {
    center: VIENNA_COORDS,
    zoom: DEFAULT_ZOOM
  };
  map = new google.maps.Map(getMapContainer(), options);
};
