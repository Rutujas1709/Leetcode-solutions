
class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        door_state = 1
        prev_time = arrival[0]

        res = [None] * len(arrival)
        res_time = arrival[0]

        priority_1_queue = []
        priority_2_queue = []

        for ind, time in enumerate(arrival):

            if time != prev_time:

                count = time - prev_time
                new_door_state = door_state
                if len(priority_1_queue) > 0 and count > 0: 
                    last_index = min(len(priority_1_queue), count) 
                    for i in range(0, last_index):
                        res[priority_1_queue[i]] = res_time 
                        res_time += 1 
                    priority_1_queue = priority_1_queue[last_index:] 
                    count -= last_index 

                if len(priority_2_queue) > 0 and count > 0: 
                    last_index = min(len(priority_2_queue), count) 
                    for i in range(0, last_index):
                        res[priority_2_queue[i]] = res_time
                        res_time += 1
                    priority_2_queue = priority_2_queue[last_index:] 
                    count -= last_index 
                    new_door_state = 1 if door_state == 0 else 0
                    priority_1_queue = priority_2_queue.copy()
                    priority_2_queue = []

                res_time += count
                door_state = 1 if count > 0 else new_door_state
                prev_time = time

            intention = state[ind]
            if (prev_time == time and intention == door_state) or (prev_time < time and intention == 1): 
                priority_1_queue.append(ind)
            else:
                priority_2_queue.append(ind) 

        
        for item in priority_1_queue:
            res[item] = res_time
            res_time += 1

        for item in priority_2_queue:
            res[item] = res_time
            res_time += 1

        return res