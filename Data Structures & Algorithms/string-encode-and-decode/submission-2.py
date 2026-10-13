class Solution:

    # encode as len(string) + # + string 
    def encode(self, strs: List[str]) -> str:
        return ''.join([str(len(s)) + '#' + s for s in strs])

    # 2-pointer approach
    def decode(self, s: str) -> List[str]:
        res = [] # init result list
        i = 0 # initialize first pointer

        while i < len(s): # limit i from going out of index
            j = i # init second pointer
            
            while s[j] != '#':
                j += 1
            
            string_length = int(s[i:j]) # convert length string encoding to int
            i = j + string_length + 1
            string_content = s[(j+1):i]

            res.append(string_content)

        return res


