class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()

        def dfs(start, target, combi):
            if target == 0:
                output.append(combi[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                dfs(i+1, target-candidates[i], combi+[candidates[i]])
        
        dfs(0, target, [])

        return output