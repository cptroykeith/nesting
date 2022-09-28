def solution(s):
    p=0
    for i in range (0,len(s)):
        if s[i]=='(':
            p+=1
        elif s[i]==')':
            p-=1
        if p < 0:
            return 0
    if p!=0:
        return 0
    else :
        return 1
