class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        :param s:
        :return: Do not return anything, modify s in-place instead
        """
        # Time: O(n) Space: O(1)
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l ,r = l + 1, r - 1

def reverse(strng):
    if len(strng) == 0:
        return ""
    else:
        return strng[len(strng)-1]+reverse(strng[0:len(strng)-1])

print(reverse('python'))