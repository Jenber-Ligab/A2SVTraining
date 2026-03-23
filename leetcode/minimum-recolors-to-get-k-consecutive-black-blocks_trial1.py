class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        white_count = blocks[:k].count('W')
        res = white_count
        for i in range(k,n):
            if blocks[i] == 'W':
                white_count += 1
            if blocks[i-k] == 'W':
                white_count -= 1
            res = min(res,white_count)
        return res