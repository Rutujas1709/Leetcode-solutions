class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        abc = sentence.lower()
        if abc != sentence:
            return False
        
        temp = set(list(abc)) 
        
        

        if len(temp) != 26:
            return False
        return True    
        



    

        