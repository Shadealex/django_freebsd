// var now = new Date();

var App = {

	init:function() {
		// App.size();
		setInterval('App.date()',1000);
	},

	size: function() {
		width=document.body.clientWidth; // ширина  
	    height=document.body.clientHeight; // высота  
	    console.log("Разрешение окна клиента: "+width+"x"+height);
	},

	date: function(){
		var options = {
			year: 'numeric',
			month: 'long',
			day: 'numeric',
			weekday: 'long',
			timezone: 'UTC',
			hour: 'numeric',
			minute: 'numeric',
			second: 'numeric'
		};

		var now = new Date();
		var time = now.toLocaleString("ru", options);
		document.getElementById('top_footer_time').innerHTML = time;
	}
}