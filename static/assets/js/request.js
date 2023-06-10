function processText(auth_token) {
  clear();
  var inputText = document.getElementById("input-text-process").value;
  var processButton = document.getElementById("process-button");
  // disable the button to prevent further processing
  //processButton.disabled = true;

  if(inputText.length == 0){
    document.getElementById("result").innerHTML = "<strong>   Please enter text in the textfield. </strong>";
    getVisible(0);
    return 0;
  }

  var xhr = new XMLHttpRequest();
  xhr.open("GET", "http://localhost:8000/process?text=" + inputText);
  xhr.setRequestHeader("Authorization", "Token " + auth_token);
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        var response = xhr.responseText;
        try {

          var result = JSON.parse(response);
          document.getElementById("result_sentiment").innerHTML = "<strong>Sentiment:</strong> " + result.sentiment.sentiment + ", <strong>Score:</strong> " + result.sentiment.score;
          getVisible(1);
        } catch (e) {
          console.log("Error parsing response:", e);
          document.getElementById("result").innerHTML = "<strong>Error parsing response.</strong>";
          getVisible(0);
        }
      } else {
        console.log("Error:", xhr.statusText);
        document.getElementById("result").innerHTML = "<strong>Error: " + xhr.statusText + "</strong>";
        getVisible(0);
      }
      
    }
  };
  xhr.send();
}

function getVisible(error_number){

    if(error_number == 0){
      document.getElementById("result").style.display = "block";
    }
    else{
      document.getElementById("result_sentiment").style.display = "block";
    }
}

function clear(){
  document.getElementById("result_sentiment").style.display = "none";
}