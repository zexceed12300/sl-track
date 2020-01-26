$(document).ready(function(){
                $("#button_continue_1").click(function(){
                    $("#button_continue_1").hide();
                    var wait_msg0 = document.getElementById("wait_msg0");
                    wait_msg0.innerHTML = "Please wait.."
                    var counter = 10;
                    var interval = setInterval(function(){
                    counter--;
                    if (counter >= 0) {
                        var wait_msg1 = document.getElementById("wait_msg1");
                        wait_msg1.innerHTML = "You will redirect in "+counter+" seconds"
                    }
                    if (counter == 0) {
                        clearInterval(interval);
                        window.location.replace("http://www.example.com/")
                    }
                    }, 1000);

                });
});