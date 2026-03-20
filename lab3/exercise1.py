from datetime import datetime


class StoryNode:
    def __init__(self, story_id, user_id, content_preview):
        self.story_id = story_id
        self.user_id = user_id
        self.content_preview = content_preview
        self.timestamp = datetime.now()
        self.views = 0
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0

    def add_story(self, new_node):
        if self.head is None:
            self.head = self.tail = self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        return "Success"

    def find_node_by_id(self, target_id):
        temp = self.head
        while temp:
            if temp.story_id == target_id:
                return temp
            temp = temp.next
        return None

    def remove_story(self, target_id):
        node = self.find_node_by_id(target_id)
        if node is None:
            return "Failed"

        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        if self.current == node:
            self.current = node.next if node.next is not None else node.prev

        self.size -= 1
        return "Success"

    def move_forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
            self.current.views += 1
            return f"Story(ID:{self.current.story_id}, Views:{self.views_of_current()})"
        return "NULL"

    def move_backward(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            self.current.views += 1
            return f"Story(ID:{self.current.story_id}, Views:{self.views_of_current()})"
        return "NULL"

    def jump_to(self, target_id):
        temp = self.head
        while temp is not None:
            if temp.story_id == target_id:
                self.current = temp
                self.current.views += 1
                return f"Story(ID:{self.current.story_id}, Views:{self.views_of_current()})"
            temp = temp.next
        return "NULL"

    def views_of_current(self):
        return self.current.views if self.current else 0



feed = DoublyLinkedList()

print(f"Action: add_story(1, 'Coffee') -> {feed.add_story(StoryNode(1, 101, 'Coffee'))}")
print(f"Final State: head={feed.head.story_id}, tail={feed.tail.story_id}, current={feed.current.story_id}\n")

print(f"Action: add_story(2, 'Work')   -> {feed.add_story(StoryNode(2, 102, 'Work'))}")
print(f"Final State: {feed.head.story_id} <-> {feed.tail.story_id}, tail={feed.tail.story_id}\n")

print(f"Action: move_forward()         -> {feed.move_forward()}")
print(f"Final State: current={feed.current.story_id}\n")

print(f"Action: move_backward()        -> {feed.move_backward()}")
print(f"Final State: current={feed.current.story_id}\n")

print(f"Action: jump_to(2)             -> {feed.jump_to(2)}")
print(f"Final State: current={feed.current.story_id}\n")

print(f"Action: remove_story(1)        -> {feed.remove_story(1)}")
state = f"{feed.head.story_id} (only)" if feed.head == feed.tail else "Multiple"
print(
    f"Final State: {state}, head={feed.head.story_id if feed.head else 'NULL'}, tail={feed.tail.story_id if feed.tail else 'NULL'}")