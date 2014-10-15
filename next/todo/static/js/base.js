var header_template = '<div class="navbar navbar-static-top">'+
				'<div class="navbar-inner">'+
					'<div class="nav-collapse" id="navItems">'+
						'<span class="title-large textGold">Todo List app</span>'+
						'<a href="/users/sign_out" class="title-small textWhite fl-r">Logout</a><br>'+
			  	  	'</div>'+
				'</div>'+
			'</div>'+
			'<div class="navbar-float"><div class="navbar-inner"></div></div>';


$(document).ready(function() {

	//Get the contents from the script block
	var source = header_template;
	//Compile that bitch
	header_template = Handlebars.compile(source);
	$(".header").html(header_template({}));


	$(".navbar-float .navbar-inner").html($("#navItems").html());
	function handleScroll(){
		if (window.XMLHttpRequest && $(window).width() > 1000){
			var offset = window.pageYOffset
			           ? window.pageYOffset
			           : document.documentElement.scrollTop;

			if (offset > 40) $(".navbar-float").fadeIn(300);
			else $(".navbar-float").fadeOut(300);
		}
	}
	if (window.addEventListener) 
		window.addEventListener('scroll', handleScroll, false);
	else 
		window.attachEvent('onscroll', handleScroll);

});
