// TODO update
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

const MAP_OPTIONS = {
  center: VIENNA_COORDS,
  zoom: DEFAULT_ZOOM,
  zoomControl: false,
  mapTypeControl: false,
  scaleControl: false,
  streetViewControl: false,
  rotateControl: false,
  fullscreenControl: false
};

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
  map = new google.maps.Map(getMapContainer(), MAP_OPTIONS);
};
