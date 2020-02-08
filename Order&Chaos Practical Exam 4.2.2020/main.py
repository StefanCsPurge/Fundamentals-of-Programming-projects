from UI import Console
from controller import Service

if __name__ == '__main__':
    # Here we build the program from its corresponding classes
    theGameController = Service()
    UserInterface = Console(theGameController)
    UserInterface.runGame()