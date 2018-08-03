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

countdown(2.9);

// convert_decimal(5.7);

// function convert_decimal(decimal) {
//   let whole_num = Math.floor(decimal)
//   let remainder = decimal - whole_num;
//   seconds = 60 * remainder;
// }
