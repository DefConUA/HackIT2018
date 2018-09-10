<?php

include 'flag.php';

$username = substr($_GET['u'],0,25);
$password = substr($_GET['p'],0,45);


echo "Hello <b>Baby:</b><br>You may need <a href=\"/?source\">this</a> and/or <a href=\"/auth.so\">this</a><br>";

if (isset($_GET['source'])){
	show_source(__FILE__);
}

$digest = @auth($username,$password);

if (md5($username) == md5($digest)  and $digest !== $username){

	echo "you are a good boy here is your flag : <b>$flag</b>";

}

else {
	echo "you are not a good boy so  no flag for you :(";
}

