$(document).ready(function() { 

    // grab your file object from a file input
    $('#uploadButton').click(function () {
        $("#status-block").hide();
        $("#gradcam").hide();
        $(".modal").modal();
        $("#loading").show();
        var form = document.getElementById('uploadAction');
        var formData = new FormData(form);
        var xhr = new XMLHttpRequest();

        xhr.onreadystatechange = function() {
            if (xhr.readyState == XMLHttpRequest.DONE) {
                results = JSON.parse(xhr.responseText);
                console.log(results);
                if(results["output"] == 0) {
                    content = "<p class='p'>Result: <i class='fa fa-check text-success'></i> Normal</p>"
                } else {
                    content = "<p class='p'>Result: <i class='fa fa-times text-danger'</i> Abnormal</p>"
                }
                setTimeout(function(){
                    $("#loading").hide();
                    $("#status").html(content);
                    $("#status-block").show();
                }, 1000);
            }
        }

        // Add any event handlers here...
        xhr.open('POST', 'http://localhost:5000', true);
        xhr.send(formData);
    });

    $("#click-details").click(function() {
        $("#status-block").hide();
        $("#gradcam").html("Gradcam will come here");
        $("#gradcam-block").children().show();
    });
});