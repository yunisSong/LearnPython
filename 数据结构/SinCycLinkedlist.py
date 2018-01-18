#coding:utf-8
class NodeTest(object):
    def __init__(self,element):
        self.element = element
        self.next = None

class SinCycLinkedlist(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        node = self.__head
        print(node.element, end=" ")
        while node.next != self.__head:
            node = node.next
            print(node.element, end=" ")
        print("")

    def add(self, item):
        """头部添加元素"""
        node = NodeTest(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            node.next = self.__head
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            self.__head = node

    def append(self, item):
        """尾部添加元素"""
        node = NodeTest(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            last = self.__head
            while last.next != self.__head:
                last = last.next
            last.next = node
            node.next = self.__head

    def insert(self, pos, item):
        if pos <= 0 :
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            count = 0
            node = NodeTest(item)
            pre = self.__head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        # 将cur指向头节点
        cur = self.__head
        pre = None
        # 若头节点的元素就是要查找的元素item
        if cur.element == item:
            # 如果链表不止一个节点
            if cur.next != self.__head:
                # 先找到尾节点，将尾节点的next指向第二个节点
                while cur.next != self.__head:
                    cur = cur.next
                # cur指向了尾节点
                cur.next = self.__head.next
                self.__head = self.__head.next
            else:
                # 链表只有一个节点
                self.__head = None
        else:
            pre = self.__head
            # 第一个节点不是要删除的
            while cur.next != self.__head:
                # 找到了要删除的元素
                if cur.element == item:
                    # 删除
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            # cur 指向尾节点
            if cur.element == item:
                # 尾部删除
                pre.next = cur.next

    def search(self, item):
        if self.is_empty():
            return False
        cur = self.__head
        if cur.element == item:
            return True
        while cur.next != self.__head:
            cur = cur.next
            if cur.element == item:
                return True
        return False

if __name__ == "__main__":
    ll = SinCycLinkedlist()
    ll.add(1)
    ll.add(2)
    ll.append(3)

    ll.travel()
    ll.travel()
    ll.travel()

    ll.insert(2, 4)
    ll.travel()
    ll.insert(4, 5)
    ll.insert(0, 6)
    print("length:", ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(7))
    ll.remove(1)
    print("length:", ll.length())
    ll.travel()
