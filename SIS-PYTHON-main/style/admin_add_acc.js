//delete
function a1() {
var x = document.getElementById("a1").value;
document.getElementById("input1").value = x;
document.getElementById("write").innerHTML="حذف";
x = document.getElementById("input3");
x.style.display = "none";
x = document.getElementById("input2");
x.style.display = "none";
x.value = "none";
}
//upload
function a2() {
var x = document.getElementById("a2").value;
document.getElementById("input1").value = x;
document.getElementById("write").innerHTML="تعديل كلمة المرور";
x = document.getElementById("input3");
x.style.display = "none";
x = document.getElementById("input2");
x.style.display = "block";
x.value = "";
}
//search
function a3() {
var x = document.getElementById("a3").value;
document.getElementById("input1").value = x;
document.getElementById("write").innerHTML="بحث";
x = document.getElementById("input3");
x.style.display = "none";
x = document.getElementById("input2");
x.style.display = "none";
x.value = "none";
}

//insert
function a4() {
var x = document.getElementById("a4").value;
document.getElementById("input1").value = x;
document.getElementById("write").innerHTML="اضافة حساب";
x = document.getElementById("input3");
x.style.display = "block";
x = document.getElementById("input2");
x.style.display = "none";
x.value = "none";
}

function a11(){
x = document.getElementById("ret");
x.style.display = "block";
}

var something = (function() {
var executed = false;
return function() {
if (!executed) {
var x = document.getElementById("a4").value;
document.getElementById("input1").value = x;
document.getElementById("write").innerHTML="اضافة حساب";
x = document.getElementById("input3");
x.style.display = "block";
x = document.getElementById("input2");
x.value = "none";
x.style.display = "none";
executed = true;
}

};
})();
something();
var myVar = setInterval(myTimer, 3000);
function myTimer() {
document.getElementById("ret3").innerHTML ="كلية الحكمة الجامعة";
}

function del() {
x = document.getElementById("ret");
x.style.display = "none";
x.value = "none";
}