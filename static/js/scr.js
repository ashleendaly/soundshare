window.onload = function (){
    var imglist = document.getElementsByClassName("outer")[0];
    var index = 0;
    var imgnub = document.getElementsByClassName("pic1");
    var imgdiv = document.getElementById("navdiv");
    var allA = document.getElementsByClassName("a1");
    var prev = document.getElementsByClassName("prev")[0];
    var next = document.getElementsByClassName("next")[0];
    imglist.style.width = 912*imgnub.length+"px";
    imgdiv.style.left= (912-5*imgnub.length)/2 + "px";
    allA[index].style.backgroundColor = "#000000";
    var timer;
    for (var i = 0; i < allA.length; i++) {
        allA[i].number = i;
        allA[i].onclick = function (){
            clearInterval(timer);
            index = this.number;
            setcolor();
            move(imglist,"left",-912*index,50,function (){
                switchbanner();
            })
        };
    }
    switchbanner();


    function setcolor(){
        if (index>=imgnub.length-1){
            index = 0;
            imglist.style.left=0;
        }
        for (var i = 0; i < allA.length; i++) {
            allA[i].style.backgroundColor="";
        }
        allA[index].style.backgroundColor="#000000";
    }

    function switchbanner(){
        timer = setInterval(function (){
            index++;
            index %= imgnub.length;
            move(imglist,"left",-912*index,15,function (){
                setcolor();
            })
        },5000)
    }
}