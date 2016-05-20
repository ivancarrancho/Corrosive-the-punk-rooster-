(function () {

		   
	
	
	
  	var loadCSS = require('./lib/loadCSS');
  	document.addEventListener('DOMContentLoaded', onDOMLoad);

  
  	function onDOMLoad() {
    
	    loadCSS('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css');
	    loadCSS('https://fonts.googleapis.com/css?family=Montserrat|Lato');
    
		var btnMenu= document.getElementById('btnMenu');
		var buttonlistclass = document.getElementById('buttonlistclass');

		btnMenu.addEventListener('click', onClickMenu);

		function onClickMenu() {
		  
			buttonlistclass.classList.toggle('button-list');
	  
		}


  }
}());
