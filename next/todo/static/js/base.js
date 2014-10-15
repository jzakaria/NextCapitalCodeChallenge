var header_template = '<div class="navbar navbar-static-top">'+
				'<div class="navbar-inner">'+
					'<div class="container">'+
						'<div class="hidden-desktop">'+
								'<img src="" width="28" height="45" style="padding-left: 40px;"></resources/img>'+
						'</div>'+
						'<div class="visible-desktop">'+
							'<table align="center">'+
								'<tr>'+
									'<td align="center">'+
										'<span class="title-large">ZETA PSI</span><br>'+
										'<span class="title-small textWhite">OMEGA ALPHA CHAPTER</span><br>'+
										'<span class="title-small textGold">UNIVERSITY OF CHICAGO</span>'+
									'</td>'+
								'</tr>'+
							'</table>'+
						'</div>'+
					'</div>'+
					'<div class="nav-collapse" id="navItems">'+
			        	'<ul class="nav">'+
							'<li class="nav_home"><a href="/omegaAlpha">HOME</a></li>'+
							'<li class="nav_about"><a href="/omegaAlpha/about">ABOUT US</a></li>'+
							'<li class="nav_rush"><a href="/omegaAlpha/rush">RUSH</a></li>'+
							'<li class="nav_brothers"><a href="/omegaAlpha/brothers">BROTHERS</a></li>'+
							'<li class="nav_parents"><a href="/omegaAlpha/parents">PARENTS</a></li>'+
							'<li class="nav_contact"><a href="/omegaAlpha/contact">CONTACT</a></li>'+
							'<li class="nav_login"><a href="/omegaAlpha/login">LOGIN</a></li>'+
			        	'</ul>'+
			  	  	'</div>'+
				'</div>'+
			'</div>'+
			'<div class="navbar-float"></div>';


$(document).ready(function() {

	//Get the contents from the script block
	var source = header_template;
	//Compile that bitch
	header_template = Handlebars.compile(source);
	$(".header").html(header_template({}));


	$(".navbar-float").html($("#navItems").html());
	function handleScroll(){
		if (window.XMLHttpRequest && $(window).width() > 1000){
			var offset = window.pageYOffset
			           ? window.pageYOffset
			           : document.documentElement.scrollTop;

			if (offset > 100) $(".navbar-float").fadeIn(300);
			else $(".navbar-float").fadeOut(300);
		}
	}
	if (window.addEventListener) 
		window.addEventListener('scroll', handleScroll, false);
	else 
		window.attachEvent('onscroll', handleScroll);

});
