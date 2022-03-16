class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = []

        max_count = 0
        count = 0

        for i in s:
            if i in table:
                if max_count < count: # new string is longer
                    max_count = count

                count = count - table.index(i)          # reset count
                table = table[table.index(i)+1 : ]      # reset table                  
            else:  
                count += 1
            table.append(i)

        if max_count < count:
            max_count = count
        return max_count
        