import os
from pytest import mark
import sys

def test_capsys(capsys):

    os.system("echo Passing test: Message to stdout - Running as subprocess")
    read = capsys.readouterr()

    assert read.out == ""

@mark.skipif(sys.platform == "win32", reason="Somente linux")
def test_capfd_linux(capfd):

    os.system("echo Passing test: Message to stdout - Running as subprocess")
    read = capfd.readouterr()

    assert read.out == "Passing test: Message to stdout - Running as subprocess\n"

@mark.skipif(sys.platform != "win32", reason="Somente windows")
def test_capfd_windowns(capfd):

    os.system("echo Passing test: Message to stdout - Running as subprocess")
    read = capfd.readouterr()

    assert read.out == "Passing test: Message to stdout - Running as subprocess\r\n"

def test_capfd_print(capfd):

    print("Function python")
    read = capfd.readouterr()

    assert read.out == "Function python\n"

def test_capfdbinary(capfdbinary):

    os.write(1,b"String binaria\n")
    captured = capfdbinary.readouterr()
    assert captured.out == b"String binaria\n"