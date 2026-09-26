from toolkit.__main__ import main


def test_calculator_cli(capsys):
    # Передаем аргументы напрямую в функцию main
    main(['calc', '2 + 2'])
    
    # Перехватываем вывод print()
    captured = capsys.readouterr()
    
    assert captured.out == "4\n"

def test_converter_cli(capsys):
    # Передаем аргументы напрямую в функцию main
    main(['convert', '30', "--from", "mm", "--to", "km"])
    
    # Перехватываем вывод print()
    captured = capsys.readouterr()
    
    assert captured.out == "0.00003\n"