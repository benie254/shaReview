function getAverage() {
var totalVotes = document.getElementById("total-votes").innerHTML;
var lastVote = document.getElementById("last-vote").innerHTML;
document.getElementById("average").innerHTML = totalVotes / lastVote;
}