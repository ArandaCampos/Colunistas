$(document).ready(function () {
    // catch the form's submit event
    $('#username').keyup(function () {
        // create an AJAX call
        $.ajax({
            data: $(this).serialize(), // get the form data
            type: 'get',
            url: "/accounts/validate-username",
            // on success
            success: function (response) {
                if (response.exist_user == true){
                    if (document.querySelector("#usernameError") === null)
                        $('.errors').append('<li class="font-small color-red" id="usernameError" >Usuário já existe</li>')
                } else {
                    $('#usernameError').remove()     
                }
            },
            // on error
            error: function (response) {
                // alert the error if any error occured
                console.log(response)
            }
        });

        return false;
    });
    
    $('#email').keyup(function () {
        // create an AJAX call
        $.ajax({
            data: $(this).serialize(), // get the form data
            type: 'get',
            url: "/accounts/validate-username",
            // on success
            success: function (response) {
                if (response.exist_email == true){
                    $('.errors').append('<li class="font-small color-red" id="emailError" >E-mail já existe</li>')
                } else {
                    $('#emailError').remove()   
                }
            },
            // on error
            error: function (response) {
                // alert the error if any error occured
                console.log(response)
            }
        });

        return false;
    });
})