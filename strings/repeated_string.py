def repeatedString(s, n):
    # Write your code here
    
    count=0
    l=len(s)
    
    if len(s)>=n:
        count=s[:n].count('a')
    else:
        c=s.count('a')
        print(c)

        div=n//len(s)
        print(div)
        rem=n % len(s)
        print(rem)
        rem_c=s[:rem].count('a')
        print(rem_c)
        
        count=(c*div)+rem_c
    #print(count)
    
    return count 

c=repeatedString("epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq",549382313570)
print(c)

n=16481469408