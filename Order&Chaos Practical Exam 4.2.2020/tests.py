import unittest
from controller import Service
"""
here we test the functionality 5
"""

class TestCheckingOrderWin(unittest.TestCase):
    def setUp(self):
        self.srv = Service()
        board = self.srv.getBoard()
        for i in range(5):
            board[i][0] = 'X'
        for j in range(1,5):
            board[2][j] = 'O'
        """
        The board is now:
          0    1    2    3    4    5
       [['X', ' ', ' ', ' ', ' ', ' '],
        ['X', ' ', ' ', ' ', ' ', ' '],
        ['X', 'O', 'O', 'O', 'O', ' '],
        ['X', ' ', ' ', ' ', ' ', ' '], 
        ['X', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        """

    def testCheckDirection(self):
        self.assertTrue(self.srv.checkDirection(1,0,1,0,'X'))
        self.assertFalse(self.srv.checkDirection(0,2,0,1,'O'))
        self.assertEqual(self.srv.checkDirection(2,2,0,1,'O',4),(2,5,'O'))

    def testFiveOrdered(self):
        self.assertTrue(self.srv.checkFiveOrdered(0,0))
        self.assertFalse(self.srv.checkFiveOrdered(0,2))

    def testOrderWin(self):
        self.assertTrue(self.srv.checkOrderWin())


if __name__ == '__main__':
    """
    K = Service()
    b = K.getBoard()
    for i in range(5):
        b[i][0] = 'X'
    for j in range(1, 5):
        b[2][j] = 'O'
    K.checkFiveOrdered(0,1)
    """
    unittest.main()
