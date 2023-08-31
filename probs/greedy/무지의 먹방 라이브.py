import heapq
def solution(food_times, k):
    heap = []
    
    if sum(food_times) <= k:
        return -1

    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i],i+1)) #첫번째 원소가 최소힙 정렬 대상
    
    prev = 0
    while heap:
        #print(k, heap[0][0], prev)
        
        if k - (heap[0][0]-prev) * len(heap) <= 0:
            break
        else:
            k -= (heap[0][0]-prev) * len(heap)
            prev = heap[0][0]
        
            heapq.heappop(heap)
    
    res = sorted(heap, key= lambda x: x[1])
    return res[k%len(heap)][1]