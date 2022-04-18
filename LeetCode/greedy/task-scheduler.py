#621. Task Scheduler
#문제 링크 : https://leetcode.com/problems/task-scheduler/

#책 풀이 : 우선순위 큐
import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            # 개수 순 추출
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub_count + 1

        return result

'''
우선순위 큐와 Counter를 이용한다. 
우선순위 큐로 가장 개수가 많은 아이템부터 하나씩 추출해야 하는데 이때 뺀 개수를 다시 업데이트 하는 과정이 필요하다.
most_common으로 가장 개수가 많은 아이템을 추출하면 task에는 해당 태스크 알파벳이 나온다.
subtract로 해당 Counter 객체에서 해당 프로세스를 뺀다. counter+=collections.Counter()는 0이나 음수를 아예
목록해서 제거하기 위한 작업이다.
most_common을 n+1로 하면 따로 예외처리를 하지 않아도 된다.


'''