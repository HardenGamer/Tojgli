<!DOCTYPE html>
<html lang="en">

<head>
	<title>Bodnar Daniel</title>
	<meta charset="utf-8" />
	{% load staticfiles %}
	<link rel="stylesheet" href="{% static 'personal/css/bootstrap.min.css' %}" type = "text/css"/>
	<meta name="viewport" content = "width=device-width, initial-scale=1.0">
	
	<style type="text/css">
		html,
		body {
		  height:100%
		}
	</style>
</head>

<body class="body" style="background-color:#f6f6f6">
	<div class="container-fluid" style="min-height:95%; ">
		<div class="row">
			  <div class="col-sm-2">
				  <br>
				  <center>
					<img src="{% static 'personal/img/profile1.jpg' %}" class="responsive-img" style='max-height:150px;' alt="face">
				  </center>
			  </div>
			  <div class="col-sm-8">
				  <br>
				  <center>
				  <h3>Programming || Gaming</h3>
				  </center>
			  </div>
			  <div class="col-sm-2">
				  <br>
				  <center>
					<img src="{% static 'personal/img/profile2.jpg' %}" class="responsive-img" style='max-height:150px;' alt="face">
				  </center>
			  </div>
		</div><hr>

		<div class="row">
		  <div class="col-sm-2">
		  <br>

		  <br>
		   <!-- Great, til you resize. -->
			<!--<div class="well bs-sidebar affix" id="sidebar" style="background-color:#fff">-->
			<div class="well bs-sidebar" id="sidebar" style="background-color:#fff">
			  <ul class="nav nav-pills nav-stacked">
				<li><a href='/'>About me</a></li>
				<li><a href='/blog/'>Blog</a></li>
				<li><a href='/contact/'>Contact</a></li>
			  </ul>
			</div> <!--well bs-sidebar affix-->
		  </div> <!--col-sm-2-->
		  <div class="col-sm-10">
		  
			<div class='container-fluid'>
			<br><br>
			   {% block content %}
			   {% endblock %}	
			</div>
		  </div>
		</div> 
	</div>
	<footer>
		<div class="container-fluid" style='margin-left:15px'>
			<p><a href="https://www.twitch.tv/200Dani" target="blank">Twitch</a> | <a href="https://www.facebook.com/profile.php?id=100007932257529" target="blank">Facebook</a> | <a href="https://www.instagram.com/bodnardaniel06/" target="blank">Instagram</a></p>
		</div>
	</footer>	
	
</body>

</html>