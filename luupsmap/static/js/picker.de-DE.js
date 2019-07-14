(function (global, factory) {
  typeof exports === 'object' && typeof module !== 'undefined' ? module.exports = factory() :
  typeof define === 'function' && define.amd ? define(factory) : factory(global.Picker);
}(typeof self !== 'undefined' ? self : this, function (Picker) {
  'use strict';

  Picker.languages['de-DE'] = {
    format: 'DD.MM.YYYY HH:mm',
    months: [
      'Januar',
      'Februar',
      'M�rz',
      'April',
      'Mai',
      'Juni',
      'Juli',
      'August',
      'September',
      'Oktober',
      'November',
      'Dezember'
    ],
    monthsShort: [
      'Jan',
      'Feb',
      'Mrz',
      'Apr',
      'Mai',
      'Jun',
      'Jul',
      'Aug',
      'Sep',
      'Okt',
      'Nov',
      'Dez',
    ],
    text: {
      title: 'Setze ein Datum oder Zeit',
      cancel: 'Abbrechen',
      confirm: 'OK',
      year: 'Jahr',
      month: 'Monat',
      day: 'Tag',
      hour: 'Stunde',
      minute: 'Minute',
      second: 'Sekunde',
      millisecond: 'Millisekunden'
    }
  };
}));
