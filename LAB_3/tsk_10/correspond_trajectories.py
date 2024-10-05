from argparse import ArgumentParser #  для обработки аргументов командной строки
import json #  для чтения файлов JSON и их конвертации в Python-объекты.


if __name__ == "__main__":
    #  Создание парсера аргументов командной строки
    parser = ArgumentParser(description="Compare two trajectories")
    parser.add_argument("true", help="true trajectory file") # эталонная траектория
    parser.add_argument("ans", help="your trajectory file") # сравниваемая таректория . Обе пути 
    args = parser.parse_args()


    # Открытие файлов и загрузка данных JSON
    with open(args.true) as f:
        true_traj = json.load(f)

    with open(args.ans) as f:
        ans_traj = json.load(f)

    if len(true_traj) != len(ans_traj): 
        """
        иначе программа выводит сообщение с указанием ожидаемой и 
        фактической длины и завершает работу с кодом ошибки 
        """
        print("Expected trajectory of length {},".format(len(true_traj)) +
              "but got trajectory of length {}".format(len(ans_traj)))
        exit(1)


    # Итерация по траекториям и их сравнение
    n = len(true_traj)
    """
    Программа проходит по всем элементам обеих траекторий, используя 
    zip(), чтобы одновременно обрабатывать элементы двух списков.
    """
    for i, p, q in zip(range(n), true_traj, ans_traj):
        if p != q:
            print("Wrong position on iteration {}".format(i))
            exit(1)

    print("OK")
