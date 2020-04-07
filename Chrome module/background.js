chrome.extension.onRequest.addListener(function(prediction){
    if (prediction == 1){
        alert("Warning: WEBSITE IS PHISHED!");
    }
    else if (prediction == -1){
        alert("WEBSITE IS SAFE!");
    }
});
