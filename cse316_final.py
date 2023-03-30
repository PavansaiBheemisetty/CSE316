from collections import deque

def round_robin(student_queue, faculty_queue, quantum):
    time = 0
    waiting_time = {}
    total_time = sum([p[1] for p in student_queue + faculty_queue])
    while student_queue or faculty_queue:
        if time >= 120:
            break
        if student_queue:
            p = student_queue.popleft()
            if p[1] > quantum:
                time += quantum
                p[1] -= quantum
                student_queue.append(p)
            else:
                time += p[1]
                if p[0] not in waiting_time:
                    waiting_time[p[0]] = time - p[1]
                else:
                    waiting_time[p[0]] += time - p[1]
                print(f"Process {p[0]} finished at {time}")
        elif faculty_queue:
            p = faculty_queue.popleft()
            if p[1] > quantum:
                time += quantum
                p[1] -= quantum
                faculty_queue.append(p)
            else:
                time += p[1]
                if p[0] not in waiting_time:
                    waiting_time[p[0]] = time - p[1]
                else:
                    waiting_time[p[0]] += time - p[1]
                print(f"Process {p[0]} finished at {time}")
        else:
            break
    return sum(waiting_time.values()) / len(waiting_time) if waiting_time else 0, time

student_queue = deque()
faculty_queue = deque()
n = int(input("Enter the number of processes: "))
for i in range(n):
    bt = int(input(f"Enter burst time for process {i+1}: "))
    priority = int(input(f"Enter priority (1 for faculty, 0 for student) for process {i+1}: "))
    if priority == 0:
        faculty_queue.append([i+1, bt])
    else:
        student_queue.append([i+1, bt])
quantum = int(input("Enter time quantum: "))
avg_waiting_time, total_time = round_robin(student_queue, faculty_queue, quantum)
if avg_waiting_time is not None:
    print(f"Average Query Time: {avg_waiting_time}")
    print(f"Total time taken: {min(total_time, 120)}")
