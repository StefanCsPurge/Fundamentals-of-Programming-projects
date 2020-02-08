from UI import Console
from controller import Service
from repo import FileRepo

if __name__ == '__main__':
    wordsRepo = FileRepo('input.txt')
    srv = Service(wordsRepo)
    app_UI = Console(srv)
    app_UI.run()



'''
Demo
word = 'abracad'
l = list(word[1:-1])
for lit in l:
    print(lit)
'''
