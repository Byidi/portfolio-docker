/* MOVE WINDOW DIV */
var mouseOrigineLeft = null;

if(document.querySelector('.window') != null){
    document.querySelector('.window .bar').addEventListener('mousedown', mouseDown, false);
    window.addEventListener('mouseup', mouseUp, false);
}

function mouseUp(){
    mouseOrigineLeft = null;
    window.removeEventListener('mousemove', windowMove, true);
}

function mouseDown(e){
    mouseOrigineLeft = e.clientX;
    window.addEventListener('mousemove', windowMove, true);
}

function windowMove(e){
    var windowDiv = document.querySelector('.window');
    var header = document.querySelector('header');
    var posTop = parseInt(e.clientY) - parseInt(header.clientHeight) - 25 - 2;
    var posLeft = parseInt(e.clientX) - ( parseInt(e.clientX) - parseInt(windowDiv.offsetLeft) );;
    windowDiv.style.top = posTop + 'px';
    windowDiv.style.left = posLeft + 'px';
    // windowDiv.style.left = (e.clientX )+ 'px';
    // console.log(windowDiv.offsetTop);
    // windowDiv.style.top = (e.clientY - windowDiv.offsetTop )+ 'px';
    // windowDiv.style.left = (e.clientX - windowDiv.offsetLeft )+ 'px';
}

/* RESIZE WINDOW DIV */

// if(document.querySelector('.window') != null){
//     document.querySelector('#resizeWindow').addEventListener('click', function(){
//         var windowDiv = document.querySelector('.window');
//         windowDiv.style.top = '0px';
//         windowDiv.style.left = '0px';
//     });
// }

//
document.querySelector('.window .bar').addEventListener('click', function(e){
    var windowDiv = document.querySelector('.window');
    var header = document.querySelector('header');
    console.log("Window Left " + windowDiv.offsetLeft);
    console.log("E Left " + e.clientX);
    var pos = parseInt(e.clientX) - ( parseInt(e.clientX) - parseInt(windowDiv.offsetLeft) );
    console.log("POS : "+ pos);
    console.log('--------------------------------');

});
