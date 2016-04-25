(function () {
  
  var loadCSS = require('./lib/loadCSS');
  
  document.addEventListener('DOMContentLoaded', onDOMLoad);

  var headerElem = document.querySelector('.header');
  
  function onDOMLoad() {
    
    var btnMenu = document.getElementById('btnMenu');
    var navbarMenu = document.getElementById('navbarMenu');

    btnMenu.addEventListener('click', onClickMenu);

    loadCSS('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css');
    loadCSS('https://fonts.googleapis.com/css?family=Montserrat|Lato');
    
    function onClickMenu() {
      navbarMenu.classList.toggle('header-menu-list--show');
    }
  }
}());
