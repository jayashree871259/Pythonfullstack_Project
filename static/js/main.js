// This runs when page loads
console.log("AI Learning System Loaded!");

// Example: Show welcome alert on Dashboard
document.addEventListener("DOMContentLoaded", function() {
    console.log("Page is ready");
});

// Example: Confirm before logout
function confirmLogout() {
    return confirm("Are you sure you want to logout?");
}

// Example: Quiz timer - 5 minutes
let timeLeft = 300;
function startTimer() {
    let timer = document.getElementById("timer");
    if (!timer) return;
    setInterval(function() {
        let min = Math.floor(timeLeft / 60);
        let sec = timeLeft % 60;
        timer.innerHTML = min + ":" + sec;
        timeLeft--;
    }, 1000);
}
startTimer();