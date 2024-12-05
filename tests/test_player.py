import unittest 
from unittest.mock import patch 
from source.player import player_pon


class TestPlayerPon(unittest.TestCase): 
    @patch('builtins.input', side_effect=['1']) 
    def test_player_hand_1(self, mock_input): 
        self.assertEqual(player_pon(), 'グー') 
        
    @patch('builtins.input', side_effect=['2']) 
    def test_player_hand_2(self, mock_input): 
        self.assertEqual(player_pon(), 'チョキ') 
        
    @patch('builtins.input', side_effect=['3']) 
    def test_player_hand_3(self, mock_input): 
        self.assertEqual(player_pon(), 'パー') 
        
    @patch('builtins.input', side_effect=['0']) 
    def test_invalid_input_0(self, mock_input): 
        with patch('builtins.input', side_effect=['1']): 
            self.assertEqual(player_pon(), 'グー') 
            
    @patch('builtins.input', side_effect=['4']) 
    def test_invalid_input_4(self, mock_input): 
        with patch('builtins.input', side_effect=['2']): 
            self.assertEqual(player_pon(), 'チョキ')
            
if __name__ == '__main__':
    unittest.main