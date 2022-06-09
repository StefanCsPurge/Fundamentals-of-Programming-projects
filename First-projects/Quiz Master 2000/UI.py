
class UI:
    def __init__(self,service):
        self.__srv = service

    def addQuestion(self,q):
        parts = q.split(';')
        if len(parts) != 7:
            raise Exception("Incorrect format!")
        self.__srv.addQuestion(parts)

    def createQuiz(self,q):
        parts = q.split()
        if len(parts) != 3:
            raise Exception("Incorrect format!")
        difficulty = parts[0]
        questionsNo = int(parts[1])
        file = parts[2]
        self.__srv.createQuiz(difficulty,questionsNo,file)

    def startQuiz(self,q):
        questions = self.__srv.getQuiz(q)
        print("Answer with a, b or c")
        choices = ('a','b','c')
        answers = []
        for q in questions:
            print(q)
            answer = input('Your answer: ').strip()
            answers.append(choices.index(answer))
        score = self.__srv.computeScore(questions,answers)
        print("Your score is {}".format(score))

    def run(self):
        print("Welcome to Quiz Master 2000! Insert your command")
        commands = {'add': self.addQuestion,
                    'create': self.createQuiz,
                    'start': self.startQuiz}
        while True:
            try:
                cmd = input(">").split()  # now cmd[0] has the type of command
                if cmd[0] not in commands:
                    raise Exception("Non-existent command!")
                commands[cmd[0]](' '.join(cmd[1:]))
            except Exception as ex:
                print(ex)