function getAverage() {
var desVotes = document.getElementById("des-v").innerHTML;
var usVotes = document.getElementById("us-v").innerHTML;
var conVotes = document.getElementById("con-v").innerHTML;
var total = parseFloat(desVotes) + parseFloat(usVotes) + parseFloat(conVotes);
var average = total / 3;
var myRounded = Number(average).toFixed(1);
document.getElementById("av").innerHTML = myRounded;
}

function copyToClip(element) {
  var $temp = $("<input>");
  $("body").append($temp);
  $temp.val($(element).text()).select();
  document.execCommand("copy");
  $temp.remove();

}