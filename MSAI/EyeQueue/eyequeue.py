import sys


class ListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev


class List:
    def __init__(self):
        self.head = ListNode(None, None, None)
        self.tail = ListNode(None, None, self.head)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.len = 0
        self.mid = self.head

    def insert(self, prev_node, val):
        if not isinstance(prev_node, ListNode):
            raise TypeError("Expected previous node to be ListNode instance")
        if prev_node.next is None:
            raise ValueError("Value error")
        new_node = ListNode(val, prev_node.next, prev_node)
        prev_node.next.prev = new_node
        prev_node.next = new_node
        if len(self) % 2 == 0:
            self.mid = self.mid.next
        self.len += 1
        return new_node

    def remove(self, node):
        if node.next is None or node.prev is None:
            raise IndexError("index error")
        node.prev.next = node.next
        node.next.prev = node.prev
        if len(self) == 1:
            self.mid = self.head
        elif len(self) % 2 == 0:
            self.mid = self.mid.next
        self.len -= 1
        return node

    def push_back(self, val):
        return self.insert(self.tail.prev, val)

    def push_front(self, val):
        return self.insert(self.head, val)

    def push_mid(self, val):
        return self.insert(self.mid, val)

    def pop_back(self):
        return self.remove(self.tail.prev).val

    def pop_front(self):
        return self.remove(self.head.next).val

    def get_node_by_index(self, i):
        if not (0 <= i < self.len + 2):
            raise IndexError("get index error")
        res = self.head
        for i in range(i):
            res = res.next
        return res

    def insert_by_index(self, i, val):
        if not isinstance(i, int):
            raise TypeError("insert type error")
        if i < 0:
            i += self.len + 1
        return self.insert(self.get_node_by_index(i), val)

    def __len__(self):
        return self.len

    def __repr__(self):
        show_len = min(len(self), 10)
        elements_repr = list(map(str, [self[i] for i in range(show_len)]))
        if len(self) > 10:
            elements_repr.append('...')
        return f"List({len(self)} elements): [{', '.join(elements_repr)}]"


if __name__ == '__main__':
    N = int(input())
    Q = [List() for i in range(N)]
    for line in sys.stdin:
        cmd = line.split()
        c_i = cmd[0]
        q_i = int(cmd[1]) if len(cmd) > 1 else None
        id_i = int(cmd[2]) if len(cmd) > 2 else None
        if c_i == '#':
            break
        elif c_i == '+':
            Q[q_i].push_back(id_i)
        elif c_i == '!':
            Q[q_i].push_mid(id_i)
        elif c_i == '-':
            print(Q[q_i].pop_front())
        elif c_i == '?':
            print(len(Q[q_i]))

