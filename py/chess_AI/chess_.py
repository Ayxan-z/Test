from chessAI import ChessAI
from chess import Board
from typing import List, Union
from os import system


def boardToMatrix(board: Board()) -> List[List[str]]:
    pgn = board.epd()
    foo = []
    pieces = pgn.split(" ", 1)[0]
    rows = pieces.split("/")
    for row in rows:
        foo2 = []
        for thing in row:
            if thing.isdigit():
                for i in range(0, int(thing)):
                    foo2.append('')
            else:
                foo2.append(thing)
        foo.append(foo2)
    return foo

def humanVsAI() -> Union[List[str], str]:
    game = ChessAI()
    print(game.board)
    l = []
    while 1:
        while 1:
            x = input('--> ')
            try: 
                game.board.push_san(x)
                break
            except: print('wrong way!')

        ctr = game.gameCheck()
        if ctr:
            print('WINNER:', ctr)
            break
        l.append(x)

        mov = game.move(3)
        game.board.push(mov)
        system('cls')
        print(game.board)
        ctr = game.gameCheck()
        if ctr:
            print('WINNER:', ctr)
            break
        l.append(mov.uci())

    print(game.board)
    return l, ctr

def AIvsAI() -> Union[List[str], str]:
    game = ChessAI()
    print(game.board)
    l = []
    while 1:
        mov = game.move(1)
        game.board.push(mov)
        ctr = game.gameCheck()
        if ctr:
            print('WINNER:', ctr)
            break
        l.append(boardToMatrix(game.board)) # mov.uci()

        mov = game.move(2)
        game.board.push(mov)
        system('cls')
        print(game.board)
        ctr = game.gameCheck()
        if ctr:
            print('WINNER:', ctr)
            break
        l.append(boardToMatrix(game.board)) # mov.uci()

    print(game.board)
    return l, ctr

if __name__ == '__main__':
    games = []
    # game_data, winner = humanVsAI() # game_data = ways(double-white, double-black), winner('Draw', 'White', 'Black')
    game_data, winner = AIvsAI()
    games.append([game_data, winner])
    print(winner)