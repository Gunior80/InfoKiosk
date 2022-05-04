 var mh = 0;
   $(".row-el").each(function () {
       var h_block = parseInt($(this).height());
       if(h_block > mh) {
          mh = h_block;
       };
   });
   $(".row-el").height(mh);

var time = setInterval(function() {
    let date = new Date();
    let hours = date.getHours();
    if (hours <= 9) hours = "0" + hours
    let minutes = date.getMinutes();
    if (minutes <= 9) minutes = "0" + minutes
    let seconds = date.getSeconds();
    if (seconds <= 9) seconds = "0" + seconds
    document.getElementById("time").innerHTML = (hours + ":" + minutes + ":" + seconds);
}, 1000);