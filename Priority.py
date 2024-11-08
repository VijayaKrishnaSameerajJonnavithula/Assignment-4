class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return f"Task(ID: {self.task_id}, Priority: {self.priority}, Arrival: {self.arrival_time}, Deadline: {self.deadline})"

class PriorityQueue:
    def __init__(self):
        self.heap = []  

    def insert(self, task):
        # Add the new task to the end of the heap
        self.heap.append(task)
        # Maintain the max-heap property
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index].priority > self.heap[parent_index].priority:
                # Swap if the current node's priority is greater than the parent's
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        # Swap the root with the last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_task = self.heap.pop()
        # Restore the heap property
        self._bubble_down(0)
        return max_task

    def _bubble_down(self, index):
        n = len(self.heap)
        while 2 * index + 1 < n:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < n and self.heap[left].priority > self.heap[largest].priority:
                largest = left
            if right < n and self.heap[right].priority > self.heap[largest].priority:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def increase_key(self, task_id, new_priority):
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                if new_priority > task.priority:
                    task.priority = new_priority
                    self._bubble_up(i)
                else:
                    task.priority = new_priority
                    self._bubble_down(i)
                return True
        return False  # Task not found

    def is_empty(self):
        return len(self.heap) == 0

# Example usage
pq = PriorityQueue()
pq.insert(Task(1, 10, '10:00', '12:00'))
pq.insert(Task(2, 5, '10:15', '12:30'))
pq.insert(Task(3, 20, '10:30', '11:00'))

print("Max task extracted:", pq.extract_max())
pq.increase_key(2, 15)
print("After increasing priority of task 2:", pq.heap)