<?php

if (isset($_POST['url']))
{
$url = $_POST['url'];
$parsed = parse_url($url);
$scheme = $parsed['scheme'];
if($scheme !== 'http'){
	die('Hacking attempt');
	}
$blacklist = ["127","local","::","http://0/"];
foreach ($blacklist as $value) {
	if (stripos($url,$value) !== false) 
		die('Hacking attempt');
}
if (substr_count($parsed['host'], '.') > 0){
	die('hacking attempt');
}

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_HEADER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, false);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$result = curl_exec($ch);
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Pee H Pee</title>
    <link rel="stylesheet" href="./static/bootstrap.min.css" />
</head>
<body>    
    <div id="main">
        <div class="container">
        </div>
        <div class="container">
            <div class="row">
                <label for="url">Enter the URL you wish to fetch:</label>
                <form class="form-inline" action="" method="post">
                    <div class="form-group">
                        <div class="input-group">
                            <div class="input-group-addon"><span class="glyphicon glyphicon-save" aria-hidden="true"></span></div>
                            <input type="text" name="url" id="url" placeholder="http://example.com/file_to_get" class="form-control" required/>
                        </div>
                        <input type="submit" name="submit" value="Submit" class="form-control btn btn-default" />
                    </div>
                </form>
            </div>
        </div>
        <?php if (isset($result) and !!$result): ?>
        <hr>
        <div class="container">
            <div class="row">    
                <div class="well">
                    <?php echo $result; ?>
                </div>
            </div>    
        </div>    
        <?php endif ?>
    </div>
</body>
</html>

