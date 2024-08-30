class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # skip non alphaNum characters from both sides
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while l < r and not self.isAlphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    def isAlphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        # conversion first:
        for c in s:
            if c.isalnum():
                newStr += c.lower()

        # comparison with reversed string
        return newStr == newStr[:: -1]  # python slice([start:stop:step])


print(Solution().isPalindrome("Was it a car or a cat I saw?"))
print(Solution().isPalindrome("tab a cat"))
