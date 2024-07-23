import pytest
from chess_puzzle import *


def test_location2index1():
    assert location2index("e2") == (5,2)

def test_index2location1():
    assert index2location(5,2) == "e2"

wr1 = Rook(3,4,True)
wk1 = King(3,5,True)


br1 = Rook(3,1,False)
bk1 = King(2,3,False)


B1 = (5, [wr1, wk1, br1, bk1])

def test_is_piece_at1():
    assert is_piece_at(2,2, B1) == False

def test_piece_at1():
    assert piece_at(3,4, B1) == wr1

def test_can_reach1():
    assert wr1.can_reach(5,4, B1) == True

def test_can_move_to1():
    assert wr1.can_move_to(5,4, B1) == False

wr1a = Rook(3,3, True)

def test_move_to1():
    Actual_B = wr1.move_to(3,3, B1)
    Expected_B = (5, [wr1a, wk1, br1, bk1]) 

    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5

    for piece1 in Actual_B[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found


    for piece in Expected_B[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found


def test_is_check1():
    B2 = (5, [wr1a, wk1, br1, bk1])
    assert is_check(False, B2) == True

def test_is_checkmate1():
    B3 = (5, [wr1a, wk1, br1, bk1, Rook(3,4, True), Rook(3,2,True)])
    assert is_checkmate(False, B3) == True

def test_read_board1():
    B = read_board("board_examp.txt")
    assert B[0] == 5

    B1 = (5, [King(2,3,False), Rook(5,3,False), King(3,5,True), Rook(4,4, True), Rook(3,1, True)])
    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

    for piece1 in B1[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
