import unittest
from unittest.mock import MagicMock, patch
import routine_calculator.command as command
import routine_calculator.global_resource as gr

class TestCommand(unittest.TestCase):

    @patch('routine_calculator.command.cmd_help.get')
    def test_help(self, mock_help_get):
        mock_help_get.return_value = "Help Message"
        self.assertTrue(command.execute("help"))
        mock_help_get.assert_called_once()

    @patch('routine_calculator.command.sys.exit')
    def test_quit(self, mock_exit):
        command.execute("quit")
        mock_exit.assert_called_once()

    @patch('routine_calculator.command.os.system')
    def test_clear(self, mock_system):
        self.assertTrue(command.execute("clear"))
        mock_system.assert_called_once()

    @patch('routine_calculator.command.cmd_pmap.print_map')
    def test_pmap(self, mock_print_map):
        self.assertTrue(command.execute("pmap"))
        mock_print_map.assert_called_once()

    @patch('routine_calculator.command.cmd_cal.print_result')
    def test_cal(self, mock_print_result):
        self.assertTrue(command.execute("cal"))
        mock_print_result.assert_called_once()

    def test_unknown_command(self):
        result = command.execute('unknown_command')
        self.assertFalse(result)

    def test_empty_command(self):
        result = command.execute('')
        self.assertTrue(result)

    @patch('routine_calculator.command.cmd_eval.simple_eval')
    def test_eval(self, mock_simple_eval):
        mock_simple_eval.return_value = 2
        command.execute('eval 1 + 1')
        mock_simple_eval.assert_called_with('1 + 1 ')


if __name__ == '__main__':
    unittest.main()
