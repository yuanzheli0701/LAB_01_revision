import time
import sys


class Comment:
    def __init__(self, text, replies=None):
        self.text = text
        self.replies = replies if replies else []


STATE_START = "START"
STATE_REPLIES_DONE = "REPLIES_DONE"


def flatten_recursive(comment):
    result = [comment.text]
    for reply in comment.replies:
        result.extend(flatten_recursive(reply))
    return result


def flatten_iterative(root_comment):
    result = []
    stack = [(root_comment, STATE_START)]
    while stack:
        current, state = stack.pop()
        if state == STATE_START:
            result.append(current.text)
            stack.append((current, STATE_REPLIES_DONE))
            for reply in reversed(current.replies):
                stack.append((reply, STATE_START))
    return result


def count_comments_tail(comment, accumulator=0):
    accumulator += 1
    if not comment.replies:
        return accumulator

    def count_list(replies_list, acc):
        if not replies_list:
            return acc
        sub_total = count_comments_tail(replies_list[0], 0)
        return count_list(replies_list[1:], acc + sub_total)

    return count_list(comment.replies, accumulator)


def count_comments_loop(root_comment):
    count = 0
    stack = [root_comment]
    while stack:
        current = stack.pop()
        count += 1
        for reply in current.replies:
            stack.append(reply)
    return count


def create_benchmark_data(depth):
    root = Comment("Root")
    curr = root
    for i in range(depth - 1):
        new_reply = Comment(f"R_{i}")
        curr.replies = [new_reply]
        curr = new_reply
    return root


def run_test_suite():
    sys.setrecursionlimit(1000)
    test_depths = [5, 10, 50, 100, 500, 1000, 2000]

    print(f"{'Depth':<10} | {'Rec (ms)':<15} | {'Iter (ms)':<15} | {'Status'}")
    print("-" * 55)

    for d in test_depths:
        node = create_benchmark_data(d)

        start = time.perf_counter()
        flatten_iterative(node)
        t_iter = (time.perf_counter() - start) * 1000

        t_rec_str = "N/A"
        status = "Success"

        try:
            start = time.perf_counter()
            flatten_recursive(node)
            t_rec = (time.perf_counter() - start) * 1000
            t_rec_str = f"{t_rec:.4f}"
        except RecursionError:
            t_rec_str = "ERROR"
            status = "StackOverflow"

        print(f"{d:<10} | {t_rec_str:<15} | {t_iter:<15.4f} | {status}")


if __name__ == "__main__":
    run_test_suite()