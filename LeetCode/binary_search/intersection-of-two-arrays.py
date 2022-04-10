#349. Intersection of Two Arrays
#문제 링크 : https://leetcode.com/problems/intersection-of-two-arrays/

#내 풀이
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1=sorted(list(set(nums1)))
        nums2=sorted(list(set(nums2)))
        
        output=[]
        
        if not nums1 or not nums2:
            return output
        
        for n in nums1:
            left, right=0, len(nums2)-1
            while left<=right:
                mid=left+(right-left)//2
                if nums2[mid]>n:
                    right=mid-1
                elif nums2[mid]<n:
                    left=mid+1
                else:
                    output.append(n)
                    break
        
        return output
                
                
'''
중복값을 제거하기 위해 set로 변환했다가 다시 list로 바꾸고 정렬을 했다.
그 다음에는 이진검색을 진행했다.
근데 이중반복문이여서 브루트 포스로 한거랑 시간이 크게 다르지 않다.
'''


#책 풀이 : 투 포인터로 일치 여부 판별
from typing import List, Set


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        # 양쪽 모두 정렬
        nums1.sort()
        nums2.sort()
        i = j = 0
        # 투 포인터 우측으로 이동하며 일치 여부 판별
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1

        return result

'''
우선 주어진 리스트를 모두 정렬한다.
만약 한쪽 배열의 값이 작으면 해당 포인터를 한칸씩 증가시킨다.
값이 같은 경우는 두 포인터 모두 증가시킨다.
비교를 하다가 한 포인터가 끝까지 가면 종료가 된다. 
'''