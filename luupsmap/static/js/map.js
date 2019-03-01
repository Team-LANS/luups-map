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
    url: `${location.href}static/svg/marker/${type}.svg`,
    scaledSize: new google.maps.Size(45, 45)
  }
};

addMarker = (venue, position) => {
  let type = venue.type;
  let marker = new google.maps.Marker({
    map,
    position,
    animation: google.maps.Animation.DROP,
    icon: getMarkerIcon(type)
  });
  marker.addListener('click', function () {
    infoWindow(venue).open(map, marker);
  });
  return marker
};

infoWindow = (venue) => {
  return new google.maps.InfoWindow({
    content: `<div>
                <p>Name: ${venue.name}</p>
                <p>Homepage: ${venue.homepage}</p>
            </div>`
  });
};

initMap = () => {
  map = new google.maps.Map(getMapContainer(), MAP_OPTIONS);
};
