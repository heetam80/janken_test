import unittest 
import random
from unittest.mock import patch 
from source.computer import computer_pon

class TestComputerPon(unittest.TestCase):
    def computer_pon(self): 
        hands = ["グー", "チョキ", "パー"] 
        computer_hand = random.choice(hands) 
        return computer_hand 

    def test_computer_pon_mocked(self): 
        with patch('random.choice', return_value="グー"): 
            assert computer_pon() == "グー", "ランダムな値が1の時に'グー'ではありません" 
        with patch('random.choice', return_value="チョキ"): 
            assert computer_pon() == "チョキ", "ランダムな値が2の時に'チョキ'ではありません" 
        with patch('random.choice', return_value="パー"): 
            assert computer_pon() == "パー", "ランダムな値が3の時に'パー'ではありません" 