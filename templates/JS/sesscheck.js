function checksessid() {
    sessid = document.getElementById('input_text').value
    console.log(sessid)
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            if(xmlHttp.responseText=="True") {
                document.body.style.backgroundColor = "red";
                return true;
            } else {
                return false;
            }
    }
    xmlHttp.open("GET", "/check/session?input_text="+encodeURIComponent(sessid), true); // true for asynchronous 
    xmlHttp.send(sessid);
}
/*
function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}
*/
//var xhr = new XMLHttpRequest();
// xhr.open('GET', "https://ipinfo.io/json", true)
// xhr.addEventListener("readystatechange", processRequest, false);