class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_queue=deque(students)
        sandwich_queue=deque(sandwiches)
        changes=0
        while student_queue and changes<len(student_queue):
            if student_queue[0]==sandwich_queue[0]:
                student_queue.popleft()
                sandwich_queue.popleft()
                changes=0
            else:
                student_queue.append(student_queue.popleft())
                changes+=1
        return len(student_queue)
        