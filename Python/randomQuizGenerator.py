# -*- coding: UTF-8 -*-
import random
import os

# 进入工作目录
os.chdir('/Users/Yunis/Desktop/学习/Python/random')
# 打印当前工作目录
print("当前工作目录为 %s"%(os.getcwd()))

# 首都以及首都集合字典 习题集及答案
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# 循环35次 因为要出35分试卷
for quizNum in range(35):
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    # 获取字典 keys
    states = list(capitals.keys())
    # 用于将一个列表中的元素打乱。
    random.shuffle(states)

    # 每份试卷有50道题目
    for questionNum in range(50):
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        # 获取答案列表
        wrongAnswers = list(capitals.values())
        # 删除正确的答案选项
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        # 从错误的答案选项随机选出3个错误的答案
        wrongAnswers = random.sample(wrongAnswers, 3)
        # 给当前题目设置答案集合
        answerOptions = wrongAnswers + [correctAnswer]
        # 打乱 答案顺序
        random.shuffle(answerOptions)
        # 在试卷文件 写入 题号 以及题目
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,states[questionNum]))
        # 在试卷文件 写入答案选项
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            
        quizFile.write('\n')
        # 把正确答案的题号以及正确答案写入答案文件
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
        answerOptions.index(correctAnswer)]))

    # 关闭试卷文件
    quizFile.close()
    # 关闭答案文件
    answerKeyFile.close()
