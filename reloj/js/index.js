    function getSecondsSinceStartOfDay() {
        return new Date().getSeconds() + 
        new Date().getMinutes() * 60 + 
        new Date().getHours() * 3600;
    }
        
    function updateClock() {
        var time = getSecondsSinceStartOfDay();
        var secondsHand = document.getElementById("seconds");
        var minutesHand = document.getElementById("minutes");
        var hourHand = document.getElementById("hour");

        var secondsRotation = time / 60 * 360;
        var minutesRotation = time / 3600 * 360;
        var hourRotation = time / 43200 * 360;

        secondsHand.style.transform = `rotate(${secondsRotation}deg)`;
        minutesHand.style.transform = `rotate(${minutesRotation}deg)`;
        hourHand.style.transform = `rotate(${hourRotation}deg)`;
    }

    setInterval(updateClock, 1000);