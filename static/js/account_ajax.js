
        $("#register-form").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    var serializedData = $(this).serialize();
    // make POST ajax call
    $.ajax({
        type: 'POST',
        url: "{% url 'register' %}",
        data: serializedData,
        success: function (response) {
            // on successfull creating object
            // alert("Successfully login")
            // window.location = "{% url 'index' %}";
            location.reload();
            window.location = window.location.href;

        },
        error: function (response) {
            // alert the error if any error occured
            element = document.querySelector('.error_text');
            document.getElementById('error_text').innerHTML = response["responseJSON"]["error"];
            // element.style.visibility = 'visible';
            // alert(response["responseJSON"]["error"]);
        }
    })
})
    




$("#login-form").submit(function (e) {
// preventing from page reload and default actions
e.preventDefault();
// serialize the data for sending the form data.
var serializedData = $(this).serialize();
// make POST ajax call
$.ajax({
type: 'POST',
url: "{% url 'login' %}",
data: serializedData,
success: function (response) {
    // on successfull creating object
    // alert("Successfully login")
    // window.location = "{% url 'index' %}";
    location.reload();
    window.location = window.location.href;

},
error: function (response) {
    // alert the error if any error occured
    element = document.querySelector('.login_error_text');
    document.getElementById('login_error_text').innerHTML = response["responseJSON"]["error"];
    // element.style.visibility = 'visible';
    // alert(response["responseJSON"]["error"]);
}
})
})







$("#forget_pass-form").submit(function (e) {
// preventing from page reload and default actions
e.preventDefault();
// serialize the data for sending the form data.
var serializedData = $(this).serialize();
// make POST ajax call
$.ajax({
type: 'POST',
url: "{% url 'forget_password' %}",
data: serializedData,
success: function (response) {
    // on successfull creating object
    // element = document.querySelector('.opt_send_message');
    // document.getElementById('opt_send_message').innerHTML = response["responseJSON"]["instance"];

    
    $('#opt_send_message').text("OTP sent to Your Mail ID");
    $('#forget_pass-form').hide();
    $('#forget_error_text').hide();
    $('#otp_confirm-form').show();
    
    // alert("Otp sent to your mail id ")
    // window.location = "{% url 'index' %}";
    // window.location = window.location.href;

},
error: function (response) {
    // alert the error if any error occured
    element = document.querySelector('.forget_error_text');
    document.getElementById('forget_error_text').innerHTML = response["responseJSON"]["error"];
    // element.style.visibility = 'visible';
    // alert(response["responseJSON"]["error"]);
}
})
})










$("#otp_confirm-form").submit(function (e) {
// preventing from page reload and default actions
e.preventDefault();
// serialize the data for sending the form data.
var serializedData = $(this).serialize();
// make POST ajax call
$.ajax({
type: 'POST',
url: "{% url 'opt_confirmation' %}",
data: serializedData,
success: function (response) {
    // on successfull creating object
    
    $('#opt_send_message').text("OTP Verified Sucessfully");
    $('#forget_pass-form').hide();
    $('#forget_error_text').hide();
    $('#otp_confirm-form').hide();
    $('#change_password-form').show();

    $("#change_pass_username").val(response["msg"]);
    console.log(response["msg"])
    // alert(response["msg"])
    
    // alert("Otp sent to your mail id ")
    // window.location = "{% url 'index' %}";
    // window.location = window.location.href;

},
error: function (response) {
    // alert the error if any error occured
    // element = document.querySelector('.forget_error_text');
    // document.getElementById('forget_error_text').innerHTML = response["responseJSON"]["error"];
    // element.style.visibility = 'visible';
    $('#opt_send_message').hide();
    $('#forget_error_text').show();
    $('#forget_error_text').text("OTP is Invalid");
    // alert(response["responseJSON"]["error"]);
}
})
})








$("#change_password-form").submit(function (e) {
// preventing from page reload and default actions
e.preventDefault();
// serialize the data for sending the form data.
var serializedData = $(this).serialize();
// make POST ajax call
$.ajax({
type: 'POST',
url: "{% url 'change_password' %}",
data: serializedData,
success: function (response) {
    // on successfull creating object
    // element = document.querySelector('.opt_send_message');
    // document.getElementById('opt_send_message').innerHTML = response["responseJSON"]["instance"];

    $('#opt_send_message').show();
    $('#opt_send_message').text("password Changed Successfully Login Now ")

    $('#forget_pass-form').hide();
    $('#forget_error_text').hide();
    $('#otp_confirm-form').hide();
    $('#change_password-form').hide();
    
    // alert("Otp sent to your mail id ")
    // window.location = "{% url 'index' %}";
    // window.location = window.location.href;

},
error: function (response) {
    // alert the error if any error occured
    // element = document.querySelector('.forget_error_text');
    // document.getElementById('forget_error_text').innerHTML = response["responseJSON"]["error"];
    // element.style.visibility = 'visible';
    $('#opt_send_message').hide();
    $('#forget_error_text').show();
    $('#forget_error_text').text("Password are not same");
    // alert(response["responseJSON"]["error"]);
}
})
})

