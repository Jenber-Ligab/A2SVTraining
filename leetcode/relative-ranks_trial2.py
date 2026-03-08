class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        '''sorted_sccore = sorted(score,reverse = True)
        output = []
        for sc in score:
            if sorted_sccore.index(sc) == 0:
                output.append("Gold Medal")
            elif sorted_sccore.index(sc) == 1:
                output.append("Silver Medal")
            elif sorted_sccore.index(sc) == 2:
                output.append("Bronze Medal")
            else: 
                output.append(str(sorted_sccore.index(sc) + 1))
        return output'''
        n = len(score)
        result = [""] * n
        sorted_score = sorted(enumerate(score), key = lambda x:x[1], reverse =True)
        for new_idx,(old_idx,value) in enumerate(sorted_score):
            if new_idx == 0:
                result[old_idx] = "Gold Medal"
            elif new_idx == 1:
                result[old_idx] = "Silver Medal"
            elif new_idx == 2:
                result[old_idx] = "Bronze Medal"
            else:
                result[old_idx] = str(new_idx + 1)
        return result





        