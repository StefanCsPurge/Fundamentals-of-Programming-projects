from domain import Question
import math
class Service:
    def __init__(self,questionsRepo):
        self.__qRepo = questionsRepo

    def addQuestion(self,parts):
        """
        Function that adds a new question to the master question list.
        :param parts: list - the elements of the question
        :return: nothing
        """
        newQ = Question(int(parts[0]),parts[1].strip(),parts[2].strip(),parts[3].strip(),parts[4].strip(),parts[5].strip(),parts[6].strip())
        self.__qRepo.add(newQ)

    def addNecessaryQuestions(self,qNo,diff):
        qList = []
        requiredDiffQ = math.ceil(qNo / 2)
        found = 0
        for q in self.__qRepo.getAll():
            if q.getDifficulty() == diff:
                if found < qNo:
                    qList.append(q)
                    found += 1
                else: break
        if found < requiredDiffQ:
            raise Exception("There are not enough questions to create the quiz!")
        return qList

    def createQuiz(self,diff,qNo,file):
        qList = self.addNecessaryQuestions(qNo,diff)
        found = len(qList)
        if found < qNo:
            for q in self.__qRepo.getAll():
                if q not in qList:
                    qList.append(q)
                    found += 1
                    if found == qNo: break
            if found < qNo:
                raise Exception("There are not enough questions!")
        f = open(file,'w')
        for q in qList:
            f.write(Question.writeQ(q)+'\n')
        f.close()

    @staticmethod
    def getQuiz(file):
        f = open(file,'r')
        qList = []
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line != "":
                qList.append(Question.readQ(line))
        f.close()
        qList.sort(key=lambda q: ('easy','medium','hard').index(q.getDifficulty()))
        return qList

    @staticmethod
    def computeScore(questions,answers):
        score = 0
        points = {'easy':1,'medium':2,'hard':3}
        n = len(questions)
        for i in range(n):
            choices = questions[i].getChoices()
            userAns = choices[answers[i]]
            if userAns == questions[i].getCorrectAns():
                score += points[questions[i].getDifficulty()]
        return score