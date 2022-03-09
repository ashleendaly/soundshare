window.onload = function (){
    var prev = document.getElementsByClassName("prev")[0];
    var next = document.getElementsByClassName("next")[0];
    var img = document.getElementsByClassName("pic1")[0];
    var imgarr = ['../static/image/github.png','../static/image/index.png']
    var index = 0;
    prev.onclick = function (){
        index--;
        if (index<0){
            index= imgarr.length-1
        }
        img.src = imgarr[index];
    }
    next.onclick = function () {
        index++;
        if(index>imgarr.length-1){
            index=0
        }
        img.src = imgarr[index];
    }
}