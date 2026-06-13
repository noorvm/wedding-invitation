const weddingDate = new Date("June 30, 2026 16:00:00");

function updateCountdown() {

    const now = new Date();

    const difference = weddingDate - now;

    const days = Math.floor(difference / (1000 * 60 * 60 * 24));

    const hours = Math.floor(
        (difference % (1000 * 60 * 60 * 24))
        / (1000 * 60 * 60)
    );

    const minutes = Math.floor(
        (difference % (1000 * 60 * 60))
        / (1000 * 60)
    );

    document.getElementById("countdown").innerHTML =
        days + " Days "
        + hours + " Hours "
        + minutes + " Minutes";
}

setInterval(updateCountdown, 1000);

updateCountdown();