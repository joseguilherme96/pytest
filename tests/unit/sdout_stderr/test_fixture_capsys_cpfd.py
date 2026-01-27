import os

def test_capsys(capsys):

    os.system("echo Passing test: Message to stdout - Running as subprocess")
    read = capsys.readouterr()

    assert read.out == ""

def test_capfd(capfd):

    os.system("echo Passing test: Message to stdout - Running as subprocess")
    read = capfd.readouterr()

    assert read.out == "Passing test: Message to stdout - Running as subprocess\n"

def test_capfd_print(capfd):

    print("Function python")
    read = capfd.readouterr()

    assert read.out == "Function python\n"

def test_capfdbinary(capfdbinary):

    os.write(1,b"String binaria\n")
    captured = capfdbinary.readouterr()
    assert captured.out == b"String binaria\n"