
var timeHandle;
   function countdown(minutes) {
    var mins = Math.floor(minutes)
    var seconds = Math.floor((minutes - mins) * 60)

   // function convert_decimal(decimal) {
   //   let whole_num = Math.floor(decimal)
   // //   let remainder = decimal - whole_num;
   //   seconds = 60 * remainder;

  if( minutes > 0 ) {
      var counter = document.getElementById("timer");


        counter.innerHTML =
        mins.toString() + ":" + (seconds < 10 ? "0" : "") + String(seconds);

            setTimeout(function () { countdown(minutes - 1.0/60); }, 1000);
        }
    
}

function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}

function checksessid() {
    document.getElementById("timer").classList.add("paused");
    document.body.style.removeProperty("-webkit-animation-play-state")
    var sessid = getCookie("sessionid");
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            if (xmlHttp.responseText != "False") {
                timeleft = xmlHttp.responseText
                countdown(xmlHttp.responseText);
                setTimeout(function(){
                    document.getElementById('Statement2').innerHTML = "to DEBATE";
                    console.log("this is happeninge??");
                    //document.body.style.webkitAnimationPlayState = "running";
                    countdown(5);
                },(timeleft*60+10)*1000)
                
                return true;
            } else {
                console.log("failed; ID not found")
                return false;
            }
    }
    xmlHttp.open("GET", "/sync?sessid=" + encodeURIComponent(sessid), true); // true for asynchronous 
    xmlHttp.send(sessid);
}

checksessid()

// convert_decimal(5.7);

// function convert_decimal(decimal) {
//   let whole_num = Math.floor(decimal)
//   let remainder = decimal - whole_num;
//   seconds = 60 * remainder;
// }
