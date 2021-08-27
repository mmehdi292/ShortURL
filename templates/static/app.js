async function copyLink(hash) {
    document.getElementById(hash).style.color = 'black'
    navigator.clipboard.writeText(window.location.origin+"/"+hash)
    var millisecondsToWait = 2000;
    setTimeout(function() {
    document.getElementById(hash).style.color = 'blue'
    }, millisecondsToWait);
}