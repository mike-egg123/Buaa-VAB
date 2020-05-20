window.onload = function () {
    //获取button对象
    var first = document.getElementById("first");
    var second = document.getElementById("second");
    var img = document.getElementsByClassName("alterimg")[0];
    var imgArray = ["../vab_img/1.png", "../vab_img/2.png", "../vab_img/3.png", "../vab_img/4.png",
        "../vab_img/5.png", "../vab_img/6.png", "../vab_img/7.png", "../vab_img/8.png"];
    var dex = 0;
    first.onclick = function () {
        dex--;
        if (dex < 0) dex = imgArray.length - 1;
        img.src = imgArray[dex];
    };
    second.onclick = function () {
        dex++;
        if (dex > imgArray.length - 1) dex = 0;
        img.src = imgArray[dex];
    };
    var iname = document.getElementById("iname");
    var iemail = document.getElementById("iemail");
    var ipassword1 = document.getElementById("ipassword1");
    var ipassword2 = document.getElementById("ipassword2");
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