
var time = setInterval(function() {
    let date = new Date();
    let hours = date.getHours();
    let minutes = date.getMinutes();
    let seconds = date.getSeconds();
    if
    document.getElementById("time").innerHTML = (hours + ":" + minutes + ":" + seconds);
    }, 1000);