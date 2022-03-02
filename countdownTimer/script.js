const daysEl = document.getElementById("days");
const hoursEl = document.getElementById("hours");
const minutesEl = document.getElementById("minutes");
const secondsEl = document.getElementById("seconds");



const newYears = "19 Mar 2022";

function diff() {
    const currentdate = new Date();
    const newYearDate = new Date(newYears);
    const diff = newYearDate - currentdate
    const totalseconds = diff / 1000;
    const days = Math.floor(totalseconds / 3600 / 24);
    const hours = Math.floor(totalseconds / 3600) % 24;
    const mins = Math.floor(totalseconds / 60) % 60;
    const seconds = Math.floor(totalseconds % 60);

    daysEl.innerHTML = formatTime(days);
    hoursEl.innerHTML = formatTime(hours);
    minutesEl.innerHTML = formatTime(mins);
    secondsEl.innerHTML = formatTime(seconds);
}
function formatTime(time) {
    return time < 10 ? `0${time}` : time;
}

setInterval(diff, 1000);
