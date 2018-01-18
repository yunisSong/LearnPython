#coding:utf-8
class NodeTest(object):
    def __init__(self,element):
        self.element = element
        self.next = None

class SingleLinkList(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        node = self.__head
        while node.next != None:
            print(node.element,end=" ")
            node = node.next

    def add(self, item):
        """头部添加元素"""
        node = NodeTest(item)
        # 下面的判断好像并不需要
        # if self.is_empty():
        #     self.__head = node
        # else:
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """尾部添加元素"""
        node = NodeTest(item)
        if self.is_empty():
            self.__head = node
        else:
            last = self.__head
            while last.next != None:
                last = last.next
            last.next = node

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
        # 记录当前节点
        cur = self.__head
        # 记录当前节点的上个节点
        pre = None
        # 如果当前节点不为空
        while cur != None:
            # 如果当前节点的数据就是要找的数据
            if cur.element == item:
               #  判断上个节点是否为空
               if pre == None:
                   # 如果上个节点为空，当前节点为链表头 直接把当前链表的头指向下一个节点
                   self.__head = cur.next
               else:
                   # 如果上一个节点不为空 把上一个节点的 next 指向当前节点的 next
                   # 当前节点就被移除了
                   pre.next = cur.next
            else:
                # 如果当前节点不是要找的节点，就继续向后找
                pre = cur
                cur = cur.next

    def search(self, item):
       cur = self.__head
       while cur != None:
            if cur.element == item:
                return True
            cur = cur.next
       return False

if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())


    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.add(100)
    ll.append(5)
    ll.append(6)
    ll.insert(2,200)
    ll.travel()
