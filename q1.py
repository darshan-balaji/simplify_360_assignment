from collections import defaultdict, deque

class TaskScheduler:
    def __init__(self, tasks, dependencies):
        # Here we are initializing the tasks, dependencies, and graph
        self.tasks = tasks
        self.dependencies = dependencies
        self.graph = defaultdict(list) 
        self.in_degree = defaultdict(int)
        self.est = {}  # Earliest Start Time for each task
        self.eft = {}  # Earliest Finish Time for each task
        self.lft = {}  # Latest Finish Time for each task
        self.lst = {}  # Latest Start Time for each task
        self.build_graph()

    def build_graph(self):
        for task in self.tasks:
            self.in_degree[task] = 0
        # Here we are bulding the graph
        for pre, succ in self.dependencies:
            self.graph[pre].append(succ)
            self.in_degree[succ] += 1

    def topological_sort(self):
        # Here we are performing topological sort using Kahn Algo
        queue = deque()
        # Add tasks with no dependencies to the queue
        for task, degree in self.in_degree.items():
            if degree == 0:
                queue.append(task)

        topological_order = []

        while queue:
            task = queue.popleft()
            topological_order.append(task)
            for successor in self.graph[task]:
                self.in_degree[successor] -= 1
                if self.in_degree[successor] == 0:
                    queue.append(successor)

        # Checking if graph is cyclic
        if len(topological_order) != len(self.tasks):
            raise ValueError("Graph has a cycle, cannot perform sort")

        return topological_order

    def calculate_earliest_times(self):
        # Here we initialize earliest start and finish times to zero
        for task in self.tasks:
            self.est[task] = 0
            self.eft[task] = 0

        # Here we are getting the topological order of tasks
        order = self.topological_sort()

        for task in order:
            # Calculating earliest start and finish times for successor tasks
            for successor in self.graph[task]:
                self.est[successor] = max(self.est[successor], self.eft[task])
                self.eft[successor] = self.est[successor] + self.tasks[successor]

    def calculate_latest_times(self):
        # Calculating the maximum earliest finish time as the project's latest completion time
        latest_completion_time = max(self.eft.values())
        for task in self.tasks:
            # Initialize latest finish and start times
            self.lft[task] = latest_completion_time
            self.lst[task] = latest_completion_time

        # Get reverse topological order of tasks
        order = self.topological_sort()[::-1]

        for task in order:
            # Calculate latest finish and start times for each task
            for successor in self.graph[task]:
                self.lft[task] = min(self.lft[task], self.lst[successor])
                self.lst[task] = self.lft[task] - self.tasks[task]

    def compute_schedule(self):
        # Calculate earliest and latest times
        self.calculate_earliest_times()
        self.calculate_latest_times()
        # Earliest and latest completion times for the entire project
        earliest_completion = max(self.eft.values())
        latest_completion = max(self.lft.values())
        return earliest_completion, latest_completion

def main():
    # Here we degine the tasks with their durations
    tasks = {
        'T_START': 0,  # Start task with zero duration
        'A': 3,
        'B': 7,
        'C': 4,
        'D': 1,
        'E': 5,
        'F': 2
    }

    # here we define dependencies between tasks
    dependencies = [
        ('T_START', 'A'),
        ('T_START', 'B'),
        ('A', 'C'),
        ('B', 'C'),
        ('B', 'D'),
        ('C', 'E'),
        ('D', 'F'),
        ('E', 'F')
    ]

    # Create TaskScheduler instance
    scheduler = TaskScheduler(tasks, dependencies)
    # Compute the earliest and latest completion times
    earliest, latest = scheduler.compute_schedule()
    print(f"Earliest completion time: {earliest}")
    print(f"Latest completion time: {latest}")

    # building the graph is O(V+E) where V is the number of taks and E is the number of dependencies
    # topological sort has time complexity of O(V+E)
    # calculating es and ls has time complexity of O(V+E)
    # hence, overall time complexity is O(V+E)
    
    # space complexity is also O(V+E)
    
if __name__ == "__main__":
    main()
