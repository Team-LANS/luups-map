'use strict';


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

const initMap = () => {
  map = new google.maps.Map(getMapContainer(), MAP_OPTIONS);
};
