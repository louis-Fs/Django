function t() {
    //alert("注册成功");
   // window.location.href="/login/";
}
function user() {
var username = document.from.lg.value;
var check=false;
var pp=/^[A-z]\w{6,18}$/;
if (pp.test(username))
	{
		var text=document.getElementsByClassName("text");
		text[0].innerHTML="OK*";
		check=true;
		return check;
	}else
	{
		var text=document.getElementsByClassName("text");
		text[0].innerHTML="用户名只能以字母开始，而不能以数字，_或$开始，字符长度大于6小于20";
		check=false;
		return check;
	}

}
/* http://www.regexlab.com/zh/regref.htm
揭开正则表达式的神秘面纱 */
function ps(){
var username = document.from.lg.value;
var pas = document.from.pass.value;
var check=false;
if(  (/^\w{6,20}$/).test(pas) && username!==pas)
	{
		var text=document.getElementsByClassName("text");
		text[1].innerHTML="OK*";
		check=true;
		return check;
	}else
	{
		var text=document.getElementsByClassName("text");
		text[1].innerHTML="密码不能和用户名相同，6<=长度<=20";
		check=false;
		return check;
	}
}
function emil(){
	var email = document.from.emi.value;
	var check=false;
	t=/^[A-z0-9\u4e00-\u9fa5]+@[A-z0-9]+(\.[A-z0-9]+)+$/;
/* 	分析邮件名称部分：
汉字在正则表示为[\u4e00-\u9fa5]
字母和数字表示为A-Za-z0-9 
通过分析得出邮件名称部分表达式为[A-Za-z0-9\u4e00-\u9fa5]+
分析邮件域名部分
邮件部分可以参考实例1中的分析域名部分。 
得出域名部分的表达式为[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+。
最终表达式： 
我们用@符号将邮箱的名称和域名拼接起来，因此完整的邮箱表达式为 ：

                        /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/
 */
if( t.test(email))
	{
		var text=document.getElementsByClassName("text");
		text[2].innerHTML="OK*";
		check=true;
		return check;
	}else
	{
		var text=document.getElementsByClassName("text");
		text[2].innerHTML="邮箱格式不正确";
		check=false;
		return check;
	}
}

var sexcheck=false;
var gradecheck=false;
function se( ) {
	var text=document.getElementsByClassName("text");
	text[4].innerHTML="OK*";
	sexcheck=true;
	return sexcheck;
}
if (!sexcheck){
	var text=document.getElementsByClassName("text");
		text[4].innerHTML="请选择性别*";
}
function gra( ) {
	var text=document.getElementsByClassName("text");
	text[5].innerHTML="OK*";
	gradecheck=true;
	return gradecheck;
}
if (!gradecheck){
	var text=document.getElementsByClassName("text");
		text[5].innerHTML="请选择年级*";
}
function phon( ) {
var username = document.from.phone.value;
var check=false;
var pp=/^[0-9]{10,11}$/;
if (pp.test(username))
	{
		var text=document.getElementsByClassName("text");
		text[6].innerHTML="OK*";
		check=true;
		return check;
	}else
	{
		var text=document.getElementsByClassName("text");
		text[6].innerHTML="输入不符合格式";
		check=false;
		return check;
	}

}
function addre( ) {
var username=document.from.address.value;
var check=false;
var pp=/^[A-z]\w{5,20}$/;
if (pp.test(username))
	{
		var text=document.getElementsByClassName("text");
		text[7].innerHTML="OK*";
		check=true;
		return check;
	}else
	{
		var text=document.getElementsByClassName("text");
		text[7].innerHTML="555555全字母吧5555";
		check=false;
		return check;
	}

}
function check() {
	var check = user() && emil() && ps() && phon() && addre() && se() && gra();
	if (check){
	    alert("注册成功****");
        //location.href='/login/';
    }
 	return check;
}