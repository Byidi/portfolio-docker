var windowBar = document.querySelector('.window .bar');
var drag = null;

document.querySelector('.window').style.top = "50px";
document.querySelector('.window').style.left = "50px";

windowBar.addEventListener("mousedown", function(){
    if(drag == null){
        document.addEventListener('mousemove', function(e){
            drag = setInterval(function(){
                moveWindow(e)
            }, 1);
        });
    }else{
        clearInterval(drag);
        drag = null;
    }
});

document.addEventListener("mouseup", function(e){
    clearInterval(drag);
    drag = null;
    console.log('reset');
});

function moveWindow(e){
    console.log('move');
    document.querySelector('.window').style.top = e.clientY+"px";
    document.querySelector('.window').style.left = e.clientX+"px";
}
