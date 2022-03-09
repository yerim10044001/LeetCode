# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_sum(node,i, num):
            while (1):
                num += node.val * i
                if node.next == None:
                    break
                node = node.next
                i *= 10
            return num

        #solution
        num1 = 0            # l1 sum
        num2 = 0            # l2 sum

        # get sum of l1
        num1 = get_sum(l1, 1, 0)
    
        # get sum of l2
        num2 = get_sum(l2, 1, 0)
        result = num1+num2
    
        # make linked List
        # head node
        r = result%10
        head = ListNode()
        head.val = r

        result = result // 10

        while (result != 0):
            node = head
            r = result % 10
            

            while node.next != None:
                node = node.next
        
            new_node = ListNode()
            new_node.val = r
            node.next = new_node
            result = result // 10
   
        
        return head