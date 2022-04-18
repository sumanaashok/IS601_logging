"""This tests the log files"""
import os


def test_request_file_created():
    """This tests if request log file is created"""
    filepath = os.path.abspath('app/logs/info.log')
    print(filepath)
    assert os.path.exists(filepath) == True


def test_debug_file_created():
    """This tests if debug log file is created"""
    filepath = os.path.abspath('app/logs/debug.log')
    print(filepath)
    assert os.path.exists(filepath) == True
