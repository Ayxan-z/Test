import chess
import chess.polyglot
from os import system

class ChessAI():
    def __init__(self):
        self.board = chess.Board()

    def __squareTables(self):
        self.pawntable = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0]
        self.knightstable = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50]
        self.bishopstable = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20]
        self.rookstable = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0]
        self.queenstable = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20]
        self.kingstable = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30]

    def gameCheck(self):
        if self.board.is_checkmate():
            if self.board.turn: return 'WINNER: Black'
            else: return 'WINNER: White'

        if self.board.is_stalemate() or self.board.is_insufficient_material(): 
            return 'Scorless'

    def __totalNumberOfPieces(self):
        self.wp = len(self.board.pieces(chess.PAWN, chess.WHITE))
        self.bp = len(self.board.pieces(chess.PAWN, chess.BLACK))
        self.wn = len(self.board.pieces(chess.KNIGHT, chess.WHITE))
        self.bn = len(self.board.pieces(chess.KNIGHT, chess.BLACK))
        self.wb = len(self.board.pieces(chess.BISHOP, chess.WHITE))
        self.bb = len(self.board.pieces(chess.BISHOP, chess.BLACK))
        self.wr = len(self.board.pieces(chess.ROOK, chess.WHITE))
        self.br = len(self.board.pieces(chess.ROOK, chess.BLACK))
        self.wq = len(self.board.pieces(chess.QUEEN, chess.WHITE))
        self.bq = len(self.board.pieces(chess.QUEEN, chess.BLACK))

    def __calculateIndividualScore(self, table, chess_piece):
        score_white = sum([table[i] for i in self.board.pieces(chess_piece, chess.WHITE)])
        score = score_white + sum([-table[chess.square_mirror(i)]
                            for i in self.board.pieces(chess_piece, chess.BLACK)])
        return score

    def __calculateScores(self):
        self.__totalNumberOfPieces()
        self.__squareTables()

        self.material = 100 * (self.wp - self.bp) + 320 * (self.wn - self.bn) + 330 *\
            (self.wb - self.bb) + 500 * (self.wr - self.br) + 900 * (self.wq - self.bq)

        self.pawnsq = self.__calculateIndividualScore(self.pawntable, chess.PAWN)
        self.knightsq = self.__calculateIndividualScore(self.knightstable, chess.KNIGHT)
        self.bishopsq = self.__calculateIndividualScore(self.bishopstable, chess.BISHOP)
        self.rooksq = self.__calculateIndividualScore(self.rookstable, chess.ROOK)
        self.queensq = self.__calculateIndividualScore(self.queenstable, chess.QUEEN)
        self.kingsq = self.__calculateIndividualScore(self.kingstable, chess.KING)

    def __evalCheck(self):
        self.__calculateScores()
        eval_ = self.material + self.pawnsq + self.knightsq +\
            self.bishopsq + self.rooksq + self.queensq + self.kingsq

        return eval_ if self.board.turn else -eval_

    def __quiesce(self, alpha, beta):
        stand_pat = self.__evalCheck()
        if (stand_pat >= beta): return beta
        if (alpha < stand_pat): alpha = stand_pat

        for move in self.board.legal_moves:
            if self.board.is_capture(move):
                self.board.push(move)
                score = -self.__quiesce(-beta, -alpha)
                self.board.pop()

                if (score >= beta): return beta

                if (score > alpha): alpha = score

        return alpha

    def __alphabeta(self, alpha, beta, depthleft):
        bestscore = -9999
        if (depthleft == 0):
            return self.__quiesce(alpha, beta)
        
        for move in self.board.legal_moves:
            self.board.push(move)
            score = -self.__alphabeta(-beta, -alpha, depthleft - 1)
            self.board.pop()
            if (score >= beta): return score
            if (score > bestscore): bestscore = score
            if (score > alpha): alpha = score
        return bestscore

    def move(self, depth):
        try:
            move = chess.polyglot.MemoryMappedReader("../data/human_chess.bin").weighted_choice(self.board).move
            return move

        except:
            bestMove = chess.Move.null()
            bestValue = -99999
            alpha = -100000
            beta = 100000
            for move in self.board.legal_moves:
                self.board.push(move)
                boardValue = -self.__alphabeta(-beta, -alpha, depth - 1)
                if boardValue > bestValue:
                    bestValue = boardValue
                    bestMove = move
                if (boardValue > alpha):
                    alpha = boardValue
                self.board.pop()
            return bestMove

def humanVsAI():
    game = ChessAI()
    print(game.board)

    while 1:
        while 1:
            x = input('--> ')
            try: 
                game.board.push_san(x)
                break
            except: print('wrong way!')

        if game.gameCheck():
            print(game.gameCheck())
            break

        mov = game.move(3)
        game.board.push(mov)
        system('cls')
        print(game.board)
        if game.gameCheck():
            print(game.gameCheck())
            break

    print(game.board)

def AIvsAI():
    game = ChessAI()
    print(game.board)

    while 1:
        mov = game.move(3)
        game.board.push(mov)
        if game.gameCheck():
            print(game.gameCheck())
            break

        mov = game.move(3)
        game.board.push(mov)
        system('cls')
        print(game.board)
        if game.gameCheck():
            print(game.gameCheck())
            break

    system('cls')
    print(game.board)

if __name__ == '__main__':
    # humanVsAI()
    AIvsAI()