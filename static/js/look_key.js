var icn_close = document.querySelector("#look-key-close")
var icn_open = document.querySelector("#look-key-open")
var input = document.querySelector("#password")

icn_close.addEventListener('click', function() {

    console.log('Clicou')
    
    input.setAttribute("type", "text")
    icn_close.classList.toggle("none")
    icn_open.classList.toggle("none")
});


icn_open.addEventListener('click', function() {

    console.log('Clicou')
    
    let input = document.querySelector("#password")

    input.setAttribute("type", "password")
    icn_close.classList.toggle("none")
    icn_open.classList.toggle("none")
});