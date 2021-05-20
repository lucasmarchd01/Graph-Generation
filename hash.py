class ClosedHashTable:
    def __init__(self, size):
        self.hasharray = [-1] * size
        self.size = size

    def hash(self, item):
        return item % self.size



    def bfspath(g, start, end):

        # Set up queue
        q = collections.deque()

        # visited vertices
        visited = {}

        # path to return
        P = []
        P.append(start)
        q.append(start, P)
        visited.add(start)
        while q:
            v, P = q.popleft()
            if v == end: # Path is found from start to end vertex.
                return P
            for n in v.neighbours:  # Iterate through neighbours.
                if n in visited:
                    continue
            next = P[:]
            next.append(n)

            v.append((n, next))

        return None # Path was not found




    def linear_probing(self, item):
        index_tracker = 0
        item_index = self.hash(item)
        final_index = item_index

        while (index_tracker < self.size) and (self.hasharray[final_index] != -1) and (
            self.hasharray[final_index] != "Deleted"):
            index_tracker += 1
            inal_index = self.hash(item_index + index_tracker)

        if (self.hasharray[final_index] == -1) or (self.hasharray[final_index] == "Deleted"):
            self.hasharray[final_index] = item

        else:
            print("Table is full, cannot insert")

    def quadratic_probing(self, item, coefficient1=1, coefficient2=1):
        index_tracker = 0
        item_index = self.hash(item)
        final_index = item_index

        while (index_tracker < self.size) and (self.hasharray[final_index] != -1) and (
            self.hasharray[final_index] != "Deleted"):
            index_tracker += 1
            final_index = (self.hash(item_index + index_tracker) + (coefficient1 * index_tracker) +
                            (coefficient2 * index_tracker ** 2)) % self.size

        if (self.hasharray[final_index] == -1) or (self.hasharray[final_index] == "Deleted"):
            self.hasharray[final_index] = item

        else:
            print("Table is full, cannot insert")

    def dh_first_hash(self, item):
        return item % self.size

    def dh_second_hash(self, item):
        return item % self.size

    def double_hashing(self, item):
        index_tracker = 0
        item_index = self.hash(item)
        final_index = item_index

        while (index_tracker < self.size) and (self.hasharray[final_index] != -1) and (
                self.hasharray[final_index] != "Deleted"):
            first_hash = self.dh_first_hash(item)
            second_hash = self.dh_second_hash(item)

            index_tracker += 1
            final_index = (first_hash + (index_tracker * second_hash)) % self.size

        if (self.hasharray[final_index] == -1) or (self.hasharray[final_index] == "Deleted"):
            self.hasharray[final_index] = item

        else:
            print("Table is full, cannot insert")

def mult_table():
    for row in range(3, 9):
        print(row, end=' ')
        for col in range(3, 9):
            print(col, end=' ')
            print(row * col, end="\t")
        print()
mult_table()