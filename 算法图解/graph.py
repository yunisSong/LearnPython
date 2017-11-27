from collections import deque


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# 判断是不是需要找到的人
def person_is_seller(name):
    if name[-1] == 'm':
        return True
    else:
        return False

# 查找与 name 关系最近的符合条件的人
def searchName(name):
    # 创建一个队列 用于存储要查找的人
    searchQueue = deque()
    # 先在 name 的第一层级去找是否有符合条件的人
    searchQueue += graph[name]
    # 用于记录 已经查找过的人 放置重复查找
    searched = []
    # 当队列不为空时，循环执行
    while searchQueue:
        # 取出队列的第一个人
        person = searchQueue.popleft()
        # 当前  person 没有被查找过
        if not person  in searched:
            print("searching " + person)
            # 判断 person 是否我们需要的人。
            if person_is_seller(person):
                print(person + " is you  need person")
                return True
            else:
                # 如果 person 不是符合条件的人
                # 把与  person 关联的人加入到队列中
                searchQueue += graph[person]
                # 把 person 标记为已经查找过
                searched.append(person)
    return False

# 查找跟 “you” 关系最近发符合条件的人。
searchName("you")
