class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict={}
        ran_dict={}
      
        for char in ransomNote:
            ran_dict[char]=ran_dict.get(char,0)+1
        for char in magazine:
            mag_dict[char]=mag_dict.get(char,0)+1
        print(ran_dict)
        print(mag_dict)
        for char in ransomNote:
            if char in magazine:
                if ran_dict[char]>mag_dict[char]:
                    return False
            if char not in magazine:
                return False
        return True
            

         
               

          
                
            
            
        return True
          
        