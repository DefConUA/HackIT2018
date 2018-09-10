This challenge is a  PHP Challenge with source code access and an extension, that implemented a custom auth function 
The extension wasn't stripped so we could easily disasemble and figure out what's happening in IDA :

Auth function :
```C
Php::Parameters *__fastcall auth(Php::Parameters *a1, __int64 a2)
{
  __int64 v2; // rax@1
  const char *v3; // rax@1
  Php::Parameters *result; // rax@1
  __int64 v5; // rbx@1
  char dest; // [sp+10h] [bp-60h]@1
  char v7[8]; // [sp+30h] [bp-40h]@1
  __int64 v8; // [sp+58h] [bp-18h]@1

  v8 = *MK_FP(__FS__, 40LL);
  strcpy(v7, "21232f297a57a5a743894a0e4a801fc3");
  LODWORD(v2) = std::vector<Php::Value,std::allocator<Php::Value>>::operator[](a2, 1LL);
  LODWORD(v3) = Php::Value::operator char const*(v2);
  strcpy(&dest, v3);
  Php::Value::Value(a1, v7, -1);
  result = a1;
  v5 = *MK_FP(__FS__, 40LL) ^ v8;
  return result;
}
```

The strcpy call will copy the second argument to the dest buffer, no size checking so this is a clear buffer overflow
The function will return what's in v7 array which is by default initialized as "21232f297a57a5a743894a0e4a801fc3"
The space between v7 and dest is ($bp-0x40) - ($bp-0x60) = 0x20 so if we write more than 0x20(32) chars into the dest buffer we can overflow the v7 buffer , thus controlling what's the function is returning .
Now let's move to the php bug, which is a trivial php type juggling, and since we control $digest value, we can make it equal to magic hash value, and exploit the type juggling vulnerability at the [line](https://github.com/DefConUA/HackIT2018/blob/master/web/PeeHPee/index.php#L17):

Using : http://host/?u=240610708&p=AAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBQNKCDZO
