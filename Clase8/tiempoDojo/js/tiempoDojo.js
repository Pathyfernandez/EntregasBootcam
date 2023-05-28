
        function mensaje() {
            alert("This page says, loading weather report ok");
        }

        function removeFooter() {
            var footer = document.querySelector("footer");
            footer.remove();
        }
    
        function convertTemperature() {
            var degreesSelect = document.getElementById("lang");
            var maxTemperatureSpans = document.querySelectorAll(".card .color1");
            var minTemperatureSpans = document.querySelectorAll(".card .color2");
            var degrees = degreesSelect.value;

            maxTemperatureSpans.forEach(function(span) {
                var temperature = parseInt(span.innerText);

                if (degrees === "Celsius") {
                    temperature = Math.round((temperature - 32) * 5 / 9);
                    span.innerText = temperature + "°C";
                } else if (degrees === "Fahrenheit") {
                    temperature = Math.round((temperature * 9 / 5) + 32);
                    span.innerText = temperature + "°F";
                }
            });
            minTemperatureSpans.forEach(function(span) {
                var temperature = parseInt(span.innerText);

                if (degrees === "Celsius") {
                    temperature = Math.round((temperature - 32) * 5 / 9);
                    span.innerText = temperature + "°C";
                } else if (degrees === "Fahrenheit") {
                    temperature = Math.round((temperature * 9 / 5) + 32);
                    span.innerText = temperature + "°F";
                }
            });

            
        }
    

