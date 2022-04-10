#240. Search a 2D Matrix II
#문제 링크 : https://leetcode.com/problems/search-a-2d-matrix-ii/

#책 풀이 - 1 : 첫 행의 맨 뒤에서 탐색
class Solution:
    def searchMatrix(self, matrix, target):
        # 예외 처리
        if not matrix:
            return False

        # 첫 행의 맨 뒤
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타겟이 작으면 왼쪽으로
            elif target < matrix[row][col]:
                col -= 1
            # 타겟이 크면 아래로
            elif target > matrix[row][col]:
                row += 1
        return False

'''
첫 행의 맨 뒤 요소를 선택한 다음에 타겟이 작으면 왼쪽으로, 크면 아래로 이동하게 한다.
'''

#책 풀이 - 2 : 한줄풀이

class Solution:
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)
'''
any()는 포함된 값 중 하나라도 참이면 True를 반환하는 함수다.
any와 유사한 함수로 all()이 있는데. all은 모든 값이 참이어야 True를 반환하는 함수다.
'''