#11286. 절댓값 힙
#문제 링크 : https://www.acmicpc.net/problem/11286

#내 풀이 - (책 풀이 보고 고쳤더니 시간초과 -> 우선순위큐대신 heapq로 고침)
import sys
import heapq

n=int(sys.stdin.readline())
queue=[]

for _ in range(n):
    now=int(sys.stdin.readline())
    if now==0:
        if not queue:
            print(0)
        else:
            print(heapq.heappop(queue)[1])            

    else:
        heapq.heappush(queue, (abs(now), now))


#책 풀이
from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline

N = int(input())
myQueue = PriorityQueue()
for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str((temp[1]))+'\n')
    else:
        # 절댓값을 기준으로 정렬하고 같으면 음수 우선 정렬하도록 구성
        myQueue.put((abs(request), request))

        
'''
그냥 큐를 쓰는 건 줄 알았는데 우선순위 큐를 써야했다.
근데 결국에 책에서 우선순위 큐에 값 넣을 때 어떻게 넣는지 보고 따라해서
거의 비슷할텐데 시간초과가 떴다. 책에서는 print를 할때 stdout.write을 사용하는데
내가 실제로 풀 때 저렇게 하지는 않을 것 같아서 검색해보니까
우선순위 큐 대신 heapq를 사용하길래 그걸로 바꿨더니 시간초과가 걸리지 않았다.
우선순위 큐에 넣을 때 (절댓값, 원래값) 형태로 넣어서 절댓값을 기준으로 정렬하는데
만약 같은 값이면 원래 값을 기준으로 정렬이 되게 한다.
'''