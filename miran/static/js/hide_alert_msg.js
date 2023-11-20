const message = document.getElementById("message")
const countdown = document.getElementById("countdown")
let opacity = 1;
let timeLeft = 5;

function updateCountdown() {
    opacity -= 0.08;
    message.style.opacity = opacity
    // countdown.innerText = timeLeft + ' сек';
    timeLeft--;

    if (timeLeft < 0) {
        message.style.display = 'none';
    }
}

const countdownTimer = setInterval(function () {
    if (timeLeft >= 0) {
        updateCountdown();
    }
}, 1000);
