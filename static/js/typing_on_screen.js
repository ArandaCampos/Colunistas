var i = 0;
var message = ""

const login = document.getElementsByName('login')
const signup = document.getElementsByName('signup')
const landingpage = document.getElementsByName('landingpage')

if (login.length){
    message = "Bem-vindo(a) ao BlogPY."
}
else if (signup.length){
    message = "Torne-se um BlogPY."
}
else if (landingpage.length){
    message = "BlogPY."
}


function typing(){
    if (i < message.length){
        document.getElementById('text').innerHTML += message.charAt(i);
        i++;
        setTimeout(typing, 100);
    }
}

typing()