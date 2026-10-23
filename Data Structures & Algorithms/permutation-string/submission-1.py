class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        permuation means both strings must be of exact same length AND same character frequencies
        '''

        # edge case: if s1 longer than s2
        if len(s1) > len(s2):
            return False

        # sliding window approach: s1-length fixed window, slide across s2
        l, r = 0, len(s1) 
        
        # store static frequency count of s1 for comparison
        s1_freq = defaultdict(int)
        for char in s1:
            s1_freq[char] += 1

        # store dynamic frequency count of s2 substrings, initialize with first substring
        s2_sub_freq = defaultdict(int)
        for char in s2[l:r]:
            s2_sub_freq[char] += 1

        while r < len(s2):
            if s2_sub_freq == s1_freq:
                return True

            # since invalid for this substring,
            # remove current leftmost element before incrementing    
            s2_sub_freq[s2[l]] -= 1
            if s2_sub_freq[s2[l]] == 0:
                del s2_sub_freq[s2[l]] # default dict will still hold key with 0 value if dont del explicitly

            # increase new rightmost element frequency
            s2_sub_freq[s2[r]] += 1 # remember r is element after the sliding window not r+1!

            # move fixed window up one element for next substring    
            r += 1
            l += 1
        
        # Check final window position after loop exits
        return s2_sub_freq == s1_freq 

