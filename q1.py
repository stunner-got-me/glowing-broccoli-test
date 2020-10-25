#Given two strings, append them together (known as "concatenation") and return the result. However, if the concatenation creates a double-char, then omit one of the chars, so "abc" and "cat" yields "abcat".
#conCat("abc", "cat") → "abcat"
#conCat("dog", "cat") → "dogcat"
#conCat("abc", "") → "abc"


def conCat(s1,s2):
    if s1=='' or s2=='':
        return s1+s2
    if s1[-1]==s2[0]:
        s=s2[1:]
        return s1+s
    return s1+s2
    
    
print(conCat('abc','cat'))
print(conCat('dog','cat'))
print(conCat('abc',''))
