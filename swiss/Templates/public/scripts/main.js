$("document").ready(function() {
    let totalPC = $("#pcNos").html()
    let username = $("#username").html()
    let password = $("#password").html()
    console.log(username,password)
    for(let i=0; i<totalPC; i++) {
        let address = $("#pc"+i).html()
        $.ajax({
            method: "POST",
            url: "http://192.168.43.222:8000/index/",
            data: JSON.stringify({
                ip: address,
                username: username,
                password: password
            })
        })
        .done((data) => {
            jsonData = JSON.parse(data)
            console.log(jsonData)
            if(jsonData.status == "1") {
                let id =  "status" + i
                $("#status" + i).addClass("online")
                $("#status" + i).html(`Online`)
            } else {
                let id =  "status" + i
                $("#status" + i).addClass("offline")
                $("#status" + i).html(`Offline`)
            }
        })
    }
});