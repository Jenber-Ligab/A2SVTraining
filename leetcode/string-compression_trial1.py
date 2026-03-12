class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        left = 0
        i = 0

        while i < n:
            char = chars[i]
            j = i

            # Count consecutive characters
            while j < n and chars[j] == char:
                j += 1
            count = j - i

            # Write the character
            chars[left] = char
            left += 1

            # Write the count if > 1
            if count > 1:
                for c in str(count):
                    chars[left] = c
                    left += 1

            # Move to next group
            i = j

        return left
            

            
        