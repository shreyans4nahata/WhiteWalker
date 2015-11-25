document.addEventListener("DOMContentLoaded", function(){
	
	console.log("TeamNaN to Rescue...!!!");
	var addbutton = document.getElementById('letsgo');
	addbutton.addEventListener('click',function() {
		console.log("Shreyansh to Rescue...!!!");
			d = document;
			var f = document.getElementById('dlform');
			f.action = 'http://akphysics.ddns.net:3032/polls/';
			var hey = 'http://akphysics.ddns.net:3032/polls/';
			f.method = 'get';
			var i = document.getElementById('song_name');

			console.log(i.value);
			f.submit();
			var the_url = hey +"?search="+i.value+"&aorv=a";
			console.log(the_url);
			chrome.downloads.download({
				url: the_url
			});
		});
	},false);

