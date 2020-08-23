from pychess import pychess as chess

game1 = chess.Game()
game1.display()

game1.move((1, 5), (2, 5))
game1.move((6, 4), (4, 4))
game1.display()

game1.move((1, 6), (3, 6))
game1.move((7, 3), (3, 7))
game1.display()
