class Solution:
    def Palindrome_List(self, lst: list)->bool:
        i=0
        n=len(lst)
        m=n-1
        while(i<n):
            if lst[i]!=lst[m]:
                return False
            m=m-1
            i=i+1
        return True
    def validPalindrome(self, s: str) -> bool:
        n=len(s)
        m=n-1
        x=0
        i=0
        lst=[]
        
        




        for a in s:
            lst.append(a)
            
        print(lst)
        while(i<n):
            if s[i]!=s[m]:
                if x<=1:
                    x+=1
                    lst1 = lst[:i] + lst[i+1:]
                    lst2 = lst[:m] + lst[m+1:]
                    print(lst1)
                    break
                else:
                     return False
            m=m-1
            i=i+1
        if x==0:
            return True
        if lst1 and lst2:
            ans1=self.Palindrome_List(lst1)
            ans2=self.Palindrome_List(lst2)
            if ans1==True or ans2==True:
                return True
            if ans1==False or ans2==False:
                return False
        
             
       