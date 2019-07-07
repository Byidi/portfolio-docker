/* MOVE WINDOW DIV */
var mouseOrigineLeft = null;
var mouseOrigineOffsetLeft = null;
var preResizeX = null;
var preResizeY = null;

if(document.querySelector('.window') != null){
    document.querySelector('.window .bar').addEventListener('mousedown', mouseDown, false);
    document.querySelector('#resizeWindow').addEventListener('click',resize, false);
    document.querySelector('.window .bar').addEventListener('dblclick',resize, false);
    window.addEventListener('mouseup', mouseUp, false);
}

function mouseUp(){
    mouseOrigineLeft = null;
    mouseOrigineOffsetLeft = null;
    window.removeEventListener('mousemove', windowMove, true);
}

function mouseDown(e){
    mouseOrigineLeft = e.clientX;
    mouseOrigineOffsetLeft = document.querySelector('.window').offsetLeft;
    window.addEventListener('mousemove', windowMove, true);
}

function windowMove(e){
    let windowDiv = document.querySelector('.window');
    let header = document.querySelector('header');
    let posTop = parseInt(e.clientY) - parseInt(header.clientHeight) - 25 - 2;
    let posLeft = windowDiv.offsetLeft + (parseInt(e.clientX) - parseInt(mouseOrigineLeft));
    posLeft = (posLeft < 0)?0:posLeft;
    mouseOrigineLeft = e.clientX;
    windowDiv.style.top = posTop + 'px';
    windowDiv.style.left = posLeft + 'px';
}

function resize(){
    let section = document.querySelector('section');
    let windowDiv = document.querySelector('.window');
    let header = document.querySelector('header');

    if(windowDiv.classList.contains('maximized')){
        windowDiv.style = "";
        windowDiv.style.top = preResizeY + "px";
        windowDiv.style.left = preResizeX + "px";

        windowDiv.classList.remove('maximized');
    }else{
        preResizeX = windowDiv.offsetLeft;
        preResizeY = windowDiv.offsetTop;

        windowDiv.style.top = section.clientHeight + 10 + "px";
        windowDiv.style.left = '0px';
        windowDiv.style.width = window.innerWidth - 2 +"px";
        windowDiv.style.height = window.innerHeight - section.clientHeight - header.clientHeight - 55 + "px";
        windowDiv.classList.add('maximized');
    }
}
