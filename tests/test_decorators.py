import os

from src.decorators import log


def test_log():
    @log()
    def logging(x):
        return x * 2
    assert logging(7) == 14


def test_log_no_file_name(capsys):
    @log()
    def logging(x):
        return x * 2
    logging(7)
    captured = capsys.readouterr()
    assert captured.out == "logging ok\n"


def test_log_error_no_filename(capsys):
    @log()
    def logging(x, y):
        return x / y
    logging(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "logging error: division by zero. Inputs: (1, 0), {}\n"


def test_log_error_str(capsys):
    @log()
    def logging(x, y):
        return x / y

    logging("7", "1")
    captured = capsys.readouterr()
    assert (
        captured.out
        == "logging error: unsupported operand type(s) for /: 'str' and 'str'. Inputs: ('7', '1'), {}\n"
    )


def test_log_good_in_file(tmp_path):
    tmp_file_path = tmp_path / "log_ok.txt"
    @log(filename=tmp_path / "log_ok.txt")
    def logging(x):
        return x * 2
    logging(7)
    assert tmp_file_path.read_text() == "logging ok\n"
    assert os.path.exists(tmp_file_path)


def test_log_error_in_file(tmp_path):
    tmp_file_path = tmp_path / "log_error.txt"
    @log(filename=tmp_path / "log_error.txt")
    def logging(x, y):
        return x / y
    logging(7, 0)
    assert tmp_file_path.read_text() == "logging error: division by zero. Inputs: (7, 0), {}\n"
    assert os.path.exists(tmp_file_path)