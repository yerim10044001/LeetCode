class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        #even odd check
        if (m+n)%2:
            case = 1    # answer is one
        else:
            case = 2    # answer is two  a + b / 2

        # make nums1 always bigger than nums2
        if m<n:
            temp = list(nums2)
            nums2 = list(nums1)
            nums1 = list(temp)
            t1 = n
            n = m
            m = t1


        ### solution ####
        m_index = (m+n-1)//2
        ######   case m>n   ######
        # i <- nums1 index
        # j <- nums2 index
        left = 0
        right = n-1
        j = right//2
        i = m_index - j

        # find middle index
        # binary search for index sum     [] + [] = middle index
        find = 1

        # if m, n == 0 exception
        if n == 0:
            answer1 = nums1[m_index]
            if case == 1 or m == 1:
                answer2 = 0
            else:
                answer2 = nums1[m_index+1]
            find = 0
        # if m, n == 1
        elif m==1 and n==1:
            answer1 = nums1[0]
            answer2 = nums2[0]
            find = 0

        # binary search start
        while(find):
            # for exception
            if j<0:
                answer1 = nums1[m_index]
                if m_index == m-1:
                    answer2 = nums2[0]
                else:
                    answer2 = nums1[m_index+1]
                break
            if left>right:
                answer1 = nums1[m_index-n]
                if case ==1:   
                    answer2 = 0
                else:
                    answer2 = nums1[m_index-n+1]
                break
            ###

            if (nums1[i] >= nums2[j]):
                if (nums1[i-1]<=nums2[j]) or i-1<0:
                    answer1 = nums2[j]
                    if (j == n-1) or (nums1[i]<nums2[j+1]):
                        answer2 = nums1[i]
                    else:
                        answer2 = nums2[j+1]
                    find = 0
                    break
                else:   #search right
                    left = j+1
                    j = (right+left)//2
                    i = m_index - j
                    continue        
            else:
                if (nums1[i] >= nums2[j-1]) or j-1<0:
                    answer1 = nums1[i]
                    if (i == m-1) or (nums2[j]<nums1[i+1]):
                        answer2 = nums2[j]
                    else:
                        answer2 = nums1[i+1]
                    find = 0
                    break
                else:   #search left
                    right = j-1
                    j = (right+left)//2
                    i = m_index - j
                    continue

        ##########
        # output #
        if case == 1:
            return(answer1)
        else:
            return((answer1+answer2)/2)



