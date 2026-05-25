import random
import time


class TrendingHeap:
    def __init__(self):
        self.heap = []
        self.position = {}

    def _higher_priority(self, a, b):
        # a and b are tuples: (likes, post_id, timestamp)
        if a[0] != b[0]:
            return a[0] > b[0]
        if a[2] != b[2]:
            return a[2] > b[2]
        return a[1] > b[1]

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.position[self.heap[i][1]] = i
        self.position[self.heap[j][1]] = j

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self._higher_priority(self.heap[index], self.heap[parent]):
                self._swap(index, parent)
                index = parent
            else:
                break

    def _heapify_down(self, index):
        n = len(self.heap)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < n and self._higher_priority(self.heap[left], self.heap[largest]):
                largest = left

            if right < n and self._higher_priority(self.heap[right], self.heap[largest]):
                largest = right

            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break

    def push(self, post_id, likes, timestamp):
        if post_id in self.position:
            self.update_likes(post_id, likes, timestamp)
            return

        entry = (likes, post_id, timestamp)
        self.heap.append(entry)
        self.position[post_id] = len(self.heap) - 1
        self._heapify_up(len(self.heap) - 1)

    def pop_max(self):
        if not self.heap:
            return None

        max_post = self.heap[0]
        last = self.heap.pop()
        del self.position[max_post[1]]

        if self.heap:
            self.heap[0] = last
            self.position[last[1]] = 0
            self._heapify_down(0)

        return max_post

    def peek_max(self):
        if not self.heap:
            return None
        return self.heap[0]

    def get_top_k(self, k):
        removed = []
        result = []

        for _ in range(min(k, len(self.heap))):
            post = self.pop_max()
            result.append(post)
            removed.append(post)

        for likes, post_id, timestamp in removed:
            self.push(post_id, likes, timestamp)

        return result

    def update_likes(self, post_id, new_likes, timestamp):
        if post_id not in self.position:
            self.push(post_id, new_likes, timestamp)
            return

        index = self.position[post_id]
        old_entry = self.heap[index]
        new_entry = (new_likes, post_id, timestamp)
        self.heap[index] = new_entry

        if self._higher_priority(new_entry, old_entry):
            self._heapify_up(index)
        else:
            self._heapify_down(index)

    def size(self):
        return len(self.heap)

    def is_valid_heap(self):
        n = len(self.heap)

        for i in range(n):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self._higher_priority(self.heap[left], self.heap[i]):
                return False

            if right < n and self._higher_priority(self.heap[right], self.heap[i]):
                return False

        return True

    def get_height(self):
        n = len(self.heap)

        if n == 0:
            return 0

        height = 0
        nodes = 1

        while nodes < n:
            height += 1
            nodes = nodes * 2 + 1

        return height

    def get_level_order(self):
        return self.heap[:]


def simulate_trending_feed():
    trending = TrendingHeap()

    for post_id in range(100):
        likes = random.randint(0, 1000)
        timestamp = int(time.time())
        trending.push(post_id, likes, timestamp)

    operations = 10000
    start_time = time.time()

    for update_number in range(1, operations + 1):
        post_id = random.randint(0, 99)
        new_likes = random.randint(0, 5000)
        timestamp = int(time.time())

        trending.update_likes(post_id, new_likes, timestamp)

        if update_number % 1000 == 0:
            top_5 = trending.get_top_k(5)
            print(f"After {update_number} updates:")
            print("Top 5 posts:", top_5)
            print()

    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / operations

    print("Heap size:", trending.size())
    print("Heap valid:", trending.is_valid_heap())
    print("Heap height:", trending.get_height())
    print("Average time per operation:", average_time)


if __name__ == "__main__":
    heap = TrendingHeap()

    heap.push("post_1", 100, 1)
    heap.push("post_2", 300, 2)
    heap.push("post_3", 200, 3)

    print("Max post:", heap.peek_max())
    print("Top 2:", heap.get_top_k(2))

    heap.update_likes("post_1", 500, 4)
    print("After update:", heap.peek_max())

    print("Valid heap:", heap.is_valid_heap())
    print("Level order:", heap.get_level_order())

    print("\nSimulation:")
    simulate_trending_feed()
