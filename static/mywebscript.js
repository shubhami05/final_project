let RunSentimentAnalysis = ()=>{
    text = document.getElementById("text").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
        if(this.status == 400){
            document.getElementById("system_response").innerHTML = "Invalid text! Please try again";
        }
    };
    xhttp.open("GET", "emotionDetector?text"+"="+text, true);
    xhttp.send();
}
