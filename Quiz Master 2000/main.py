from UI import UI
from controller import Service
from repo import FileRepo
from domain import Question

if __name__ == '__main__':
    questionsRepo = FileRepo("questionsMaster.txt",Question.readQ,Question.writeQ)
    srv = Service(questionsRepo)
    app_UI = UI(srv)
    app_UI.run()