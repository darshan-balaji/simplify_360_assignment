from collections import deque, defaultdict

class FriendshipNetwork:
    def __init__(self):
        # Here we initialize the friendship network as a dictionary
        self.network = defaultdict(set)

    def add_friendship(self, person1, person2):
        # This code adds the bidirectional friendship between person1 and person2
        self.network[person1].add(person2)
        self.network[person2].add(person1)

    def find_friends(self, person):
        # Here we return the set of friends for a given person
        return self.network[person]

    def find_common_friends(self, person1, person2):
        # Here we return the intersection of friends of person1 and person2
        return self.network[person1].intersection(self.network[person2])

    def find_nth_connection(self, start_person, target_person):
        # If both people are the same, the connection level is 0
        if start_person == target_person:
            return 0

        # Use BFS to find the shortest connection level
        visited = set()  # Set to keep track of visited people
        queue = deque([(start_person, 0)])  # Queue holds tuples of (person, connection_level)

        while queue:
            current_person, level = queue.popleft()

            # If the target person is found, return the connection level
            if current_person == target_person:
                return level

            visited.add(current_person)

            # Explore friends of the current person
            for friend in self.network[current_person]:
                if friend not in visited:
                    queue.append((friend, level + 1))
                    visited.add(friend)

        # Return -1 if no connection is found
        return -1

def main():
    # Create a friendship network
    network = FriendshipNetwork()

    # Add friendships
    network.add_friendship('Alice', 'Bob')
    network.add_friendship('Bob', 'Janice')
    network.add_friendship('Alice', 'Charlie')
    network.add_friendship('Charlie', 'David')
    network.add_friendship('David', 'Eve')
    network.add_friendship('Janice', 'Grace')

    # Find friends
    alice_friends = network.find_friends('Alice')
    bob_friends = network.find_friends('Bob')
    print(f"Friends of Alice: {alice_friends}")
    print(f"Friends of Bob: {bob_friends}")

    # Find common friends
    common_friends = network.find_common_friends('Alice', 'Bob')
    print(f"Common friends of Alice and Bob: {common_friends}")

    # Here we find the nth connection
    connection_level = network.find_nth_connection('Alice', 'Janice')
    print(f"Connection level between Alice and Janice: {connection_level}")

    connection_level = network.find_nth_connection('Alice', 'Bob')
    print(f"Connection level between Alice and Bob: {connection_level}")

    connection_level = network.find_nth_connection('Alice', 'Grace')
    print(f"Connection level between Alice and Grace: {connection_level}")

    connection_level = network.find_nth_connection('Alice', 'Eve')
    print(f"Connection level between Alice and Eve: {connection_level}")

    #adding friendship and finding common friends has time complexity of O(1)
    #finding common friends has a time complexity of O(min(f1,f2)) where f1 and f2 are the number of friends person1 and person2 have respectively
    #finding nth connection has complexity of )(V+e) where V is the number of people and E is the number of friendships, vertices and edges respectively
    
    #space complexity is O(V+E)
    
if __name__ == "__main__":
    main()
