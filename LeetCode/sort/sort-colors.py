#75. Sort Colors
#문제 링크 : https://leetcode.com/problems/sort-colors/

#내 풀이 : 성공X
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp=nums[:]
        nums=[tmp[0]]
        
        del tmp[0]
        
        def insert_sort(num):
            for i in range(len(nums)-1, -1, -1):

                if i-1>-1:
                    if nums[i]>=num and nums[i-1]<=num:
                        nums.insert(i, num)
                        break
                    elif nums[i]<num:
                        nums.append(i)
                        break
                else:
                    if nums[i]<=num:
                        nums.append(num)
                        break
                    else:
                        nums.insert(i, num)
                        break
            
        
        for t in tmp:
            insert_sort(t)

'''
print(nums)를 하면 답과 일치하는데 nums의 값을 바꾸는 방식으로 해서
정답으로 인정되지 않는 것 같다.
'''

#책 풀이 : 퀵 정렬 개선 알고리즘
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)

        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1

'''
피벗보다 작은부분, 같은부분, 큰부분 이렇게 세부분으로 분할해서 정렬한다.
포인터가 red, white, blue로 3개다. red, white는 0에서 시작하고 blue는 끝에서 시작한다.
0, 1, 2 중 중간값인 1을 기준으로 비교를 한다. 그래서 nums[white]가 비교대상 값이 된다.
1보다 작으면 왼쪽으로, 큰 값은 오른쪽으로 스왑된다.
red는 점점 오른쪽, blue는 왼쪽으로 이동하면서 가까워진다.
비교가 완료되면 red는 1보다 작은 인덱스의 +1지점, blue는 1보다 큰 인덱스의 시작점을 가리키고
white와 blue는 같아진다.
'''
            
