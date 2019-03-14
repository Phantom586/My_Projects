var header = document.querySelector("h1");
var btn_1 = document.querySelector("#btn_1");
var btn_2 = document.querySelector("#btn_2");

console.log('connected!');
var decide = false;

function getRandomColor () {
    var letters = "01234567ABCDEF";
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random()*16)];
    }
    return color;
}

function changeHeaderColor () {
    colorInput = getRandomColor()
    header.style.color = colorInput;
}

btn_1.addEventListener("click", function () {
    timer = setInterval("changeHeaderColor()", 500);
});

btn_2.addEventListener("click", function () {
    clearInterval(timer);
    header.style.color = 'black';
});