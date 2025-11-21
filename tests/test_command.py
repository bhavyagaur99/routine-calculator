import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import command

class TestCommand(unittest.TestCase):

    @patch('command.cmd_help')
    def test_help(self, mock_help):
        command.execute('help')
        mock_help.get.assert_called_once()

    @patch('command.cmd_pmap')
    def test_pmap(self, mock_pmap):
        command.execute('pmap')
        mock_pmap.print_map.assert_called_once()

    @patch('command.cmd_cal')
    def test_cal(self, mock_cal):
        command.execute('cal')
        mock_cal.print_result.assert_called_once()

    def test_unknown_command(self):
        result = command.execute('unknown_command')
        self.assertFalse(result)

    def test_empty_command(self):
        result = command.execute('')
        self.assertTrue(result)

    @patch('command.cmd_eval')
    def test_eval(self, mock_eval):
        mock_eval.simple_eval.return_value = 2
        command.execute('eval 1 + 1')
        mock_eval.simple_eval.assert_called_with('1 + 1 ')

    @patch('command.sys.exit')
    def test_quit(self, mock_exit):
        command.execute('quit')
        mock_exit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
