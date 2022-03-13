$(document).ready(function (){
    $("input[id = 'uploadreason']").focus(function () {
        $('#uploadfile').animate({
            "width": "400px",
            "height": "70px",
        })
    }).blur(function (){
        $('#uploadfile').animate({
            "height": "54px",
	        "width": "100%",
        })
    });
});