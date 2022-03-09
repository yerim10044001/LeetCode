class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # (key, index) array
        a = []

        count = 0
        for i in nums:
            a.append([])
            a[count].append(i)
            a[count].append(count)
            count += 1

        # sort list a
        a.sort(key=lambda x:x[0])

        # find solution
        i = 0
        j = len(nums)-1
        result =[]
        while (1):
            sum = a[i][0] + a[j][0]
            if sum < target :
                i += 1
                continue
            elif sum > target:
                j -= 1
                continue
            else:
                break
        if(a[i][1] < a[j][1]):
            result.append(a[i][1])
            result.append(a[j][1])
        else:
            result.append(a[i][1])
            result.append(a[j][1])
        return result

