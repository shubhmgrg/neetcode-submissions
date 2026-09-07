class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = s.strip().lower()
        i = 0
        print(new)
        while i < len(new):
            if not new[i].isalnum():
                new = new[:i] + new[i+1:]
            else:
                i += 1
            print(new)

        if new == new[::-1]:
            return True
        return False