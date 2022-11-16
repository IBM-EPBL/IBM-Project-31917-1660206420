<?php

session_start();


$con=mysqli_connect('localhost','root','toor');

mysqli_select_db($con,'userregistration');

$name=$_POST['user'];

$pass=$_POST['password'];

$s="select * from usertable where name='$name' && password='$pass'";
$result=mysqli_query($con,$s);
$num=mysqli_num_rows($result);

if($num==1){

	header('location:index.html');
}else{
	
	echo "you r new here";
	
	
}
?>