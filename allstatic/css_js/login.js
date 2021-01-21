
function validateLogin () {
    var username = document.login.user.value;
    var pas = document.login.pass.value;
    var check1=false;
    var check=false;
var pp=/^[A-z]\w{6,18}$/;
if (pp.test(username))
	{
		var text=document.getElementsByClassName("text");
		text[1].innerHTML="OK*";
		check=true;
	}else
	{
		var text=document.getElementsByClassName("text");
		text[1].innerHTML="提醒：用户名只能以字母开始，而不能以数字，_或$开始，字符长度大于6小于20";
		check=false;
	}
if(  (/^\w{6,20}$/).test(pas) && username!==pas)
	{
		var text=document.getElementsByClassName("text");
		text[2].innerHTML="OK*";
		check1=true;

	}else
	{
		var text=document.getElementsByClassName("text");
		text[2].innerHTML="提醒：6<=长度<=20";
		check1=false;
	}
     return check && check1;
}
