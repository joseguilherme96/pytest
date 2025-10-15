def coodernada_drone(name):
    print(f"Latitude : 1002022; Longitude : 223333!")

def test_coodernada_drone(capsys):
    coodernada_drone("Latitude : 1002022; Longitude : 223333!")
    captured = capsys.readouterr()
    assert captured.out == "Latitude : 1002022; Longitude : 223333!\n"
