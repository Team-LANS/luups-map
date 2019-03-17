'use strict';


const VIENNA_COORDS = {
  lat: 48.208176,
  lng: 16.373819
};

const DEFAULT_ZOOM = 15;

const MAP_STYLE = [
  {
    elementType: 'geometry.fill',
    stylers: [
      {saturation: -75},
      {lightness: 50}
    ]
  },
  {
    elementType: 'geometry.stroke',
    stylers: [
      {saturation: -75},
      {lightness: 25}
    ]
  },
  {
    elementType: 'labels.icon',
    stylers: [
      {saturation: -75},
      {lightness: 13}
    ]
  },
  {
    elementType: 'labels.text',
    stylers: [
      {saturation: -75},
      {lightness: 25}
    ]
  }
];

const MAP_OPTIONS = {
  center: VIENNA_COORDS,
  zoom: DEFAULT_ZOOM,
  styles: MAP_STYLE,
  zoomControl: false,
  mapTypeControl: false,
  scaleControl: false,
  streetViewControl: false,
  rotateControl: false,
  fullscreenControl: false
};

let map;  // the map object
let currentInfoWindow;

// FUNCTIONS ///////////////////////////////////////////////////////////////////////////////////////////////////////////

const getMapContainer = () => document.getElementById('map');

const getMarkerIcon = (type) => {
  return {
    url: `${location.href}static/svg/marker/${type}.svg`,
    scaledSize: new google.maps.Size(45, 45)
  }
};

const addMarker = (venue, position) => {
  let type = venue.type;
  let marker = new google.maps.Marker({
    map,
    position,
    animation: google.maps.Animation.DROP,
    icon: getMarkerIcon(type)
  });
  marker.addListener('click', () => {
    openInfoWindow(venue, marker);
  });
  return marker;
};

const openInfoWindow = (venue, marker) => {
  if (currentInfoWindow) {
    currentInfoWindow.close();
  }

  const title = `<h5>${venue.name}</h5>`;
  const links = createUrlLinks(venue.homepage);
  const details = `<a class="btn--green btn--s" href="${venue.href}">Details anzeigen</a>`;
  currentInfoWindow = new google.maps.InfoWindow({
    content: `<article class="info-window">${title}${links}<br>${details}</article>`
  });
  currentInfoWindow.open(map, marker);
};

const createUrlLinks = (links) => {
  return links.split(', ').map(link => getUrlLink(link)).join('<br>');
};

const getUrlLink = (link) => {
  const linkText = link.replace(/^(https?:\/\/)/, '').replace(/^(www\.)/, '').replace(/\/$/, '');
  const url = link.startsWith('http') ? link : `http://${link}`;

  return `<a href="${url}">${linkText}</a>`;
};

const filterControl = (controlDiv) => {
  // Set CSS for the control border.

  let filter = document.getElementById('filter');
  let controlUI = document.createElement('div');
  controlDiv.appendChild(controlUI);
  controlUI.appendChild(filter);
  controlUI.addEventListener('click', function () {
    showModal(true)
  });
};

const initMap = () => {
  map = new google.maps.Map(getMapContainer(), MAP_OPTIONS);
  let filterControlDiv = document.createElement('div');
  filterControl(filterControlDiv);

  filterControlDiv.index = 1;
  map.controls[google.maps.ControlPosition.TOP_RIGHT].push(filterControlDiv);
};
