'use strict';


/* Get the modal */

const showModal = (value) => {
  const modal = document.getElementById('modal');
  const overlay = document.getElementById('overlay');
  if (value) {
    modal.classList.add('visible');
    overlay.classList.add('visible')
  }
  else {
    modal.classList.remove('visible');
    overlay.classList.remove('visible')
  }
};

