var header = $('h1');
var btn_1 = $('#btn_1');
var btn_2 = $('#btn_2');

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
    header.css('color', colorInput);
}

btn_1.on('click', function () {
    timer = setInterval("changeHeaderColor()", 500);
});

btn_2.on('click', function () {
    clearInterval(timer);
    header.css('color', 'black');
});

