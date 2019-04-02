let address = $("#pcAddr").html()
let username = $("#username").html()
let password = $("#password").html()
$("document").ready(() => {  
    console.log(address)
    $.ajax({
        method:"POST",
        url: "http://192.168.43.222:8000/getram/",
        data: JSON.stringify({
            ip: address,
            username: username,
            password: password
        })
    })
    .done((data) => {
        jsonData = JSON.parse(data)
        console.log(jsonData)
        $("#free-ram").html(jsonData.ram["3"]);
        $("#total-ram").html(jsonData.ram["0"]);
    })
})

$("#send").click(() => {
    let text  = $("#text").val();
    console.log(text)
    $.ajax({
        method:"POST",
        url: "http://192.168.43.222:8000/sendmessage/",
        data: JSON.stringify({
            ip: address,
            username: username,
            password: password,
            text: text
        })
    }) 
})

$("#dirSend").click(() => {
    $("#content").html("-")
    let text  = $("#dir-text").val();
    console.log(text)
    $.ajax({
        method:"POST",
        url: "http://192.168.43.222:8000/ls/",
        data: JSON.stringify({
            ip: address,
            username: username,
            password: password,
            text: text
        })
    })
    .done((data) => {
        let jsonData = JSON.parse(data)
        console.log(jsonData.files)
        jsonData.files.forEach((data) => {
            $("#content").append(data + "<br>")
        })
    });
})

$("#dirClear").click(() => {
    $("#content").html("-")
});