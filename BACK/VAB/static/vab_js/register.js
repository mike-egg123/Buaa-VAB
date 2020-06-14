window.onload = function () {
    //获取button对象
    var iname = document.getElementById("username");
    var iemail = document.getElementById("email");
    var ipassword1 = document.getElementById("password_1");
    var ipassword2 = document.getElementById("password_2");
    if (ipassword1.value != ipassword2.value)
        alert("两个密码不一致！");
    var btn01 = document.getElementById("ilogin-btn");
    var myalert01 = document.getElementById("myalert01");
    var myalert02 = document.getElementById("myalert02");
    btn01.onclick = function () {
        if (iemail.value == "" || iname.value == "" || ipassword1.value == "" || ipassword2.value == "") {
            // myalert01.className = "in";
            alert("不能有空！");
        }
        else if (ipassword1.value != ipassword2.value) {
            alert("两个密码不一致！");
        }
        else
            alert("提交成功！");
    };
};