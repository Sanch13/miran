const message = document.getElementById("message")

if (message) {
    let opacity = 1;
    let timeLeft = 5;

    function updateCountdown() {
        opacity -= 0.08;
        message.style.opacity = opacity
        timeLeft--;

        if (timeLeft < 0) {
            message.style.display = 'none';
            clearInterval(countdownTimer);
        }
    }

    const countdownTimer = setInterval(function () {
        if (timeLeft >= 0) {
            updateCountdown();
        }
    }, 1000);
}
