import os
import subprocess
import time
import sys

# Пути к скриптам и файлам
VITERBI_SCRIPT = 'generate_viterbi_trajectory.py'
COMPARE_SCRIPT = 'correspond_trajectories.py'
GRAPH_FILE = 'graph.ldj'
CONFIG_FILE = 'localization_config.json'
TRUE_TRAJECTORY = 'true_trajectory.json'
OUTPUT_TRAJECTORY = 'output_trajectory.json'

def run_viterbi():
    """
    Запуск скрипта генерации траектории с помощью Viterbi алгоритма.
    Возвращает время выполнения.
    """
    start_time = time.time()

    # Запуск скрипта генерации траектории
    process = subprocess.run([sys.executable, VITERBI_SCRIPT, GRAPH_FILE, CONFIG_FILE, OUTPUT_TRAJECTORY], 
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    end_time = time.time()
    elapsed_time = end_time - start_time

    if process.returncode != 0:
        print(f"Ошибка при выполнении {VITERBI_SCRIPT}:")
        print(process.stderr.decode())
        sys.exit(1)

    print(f"Время выполнения Viterbi: {elapsed_time:.2f} секунд")
    return elapsed_time

def compare_trajectories():
    """
    Запуск скрипта сравнения траекторий.
    """
    process = subprocess.run([sys.executable, COMPARE_SCRIPT, TRUE_TRAJECTORY, OUTPUT_TRAJECTORY], 
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if process.returncode != 0:
        print(f"Ошибка при выполнении {COMPARE_SCRIPT}:")
        print(process.stderr.decode())
        sys.exit(1)

    # Вывод результата сравнения
    print(process.stdout.decode())

if __name__ == "__main__":
    # 1. Запуск генерации траектории с замером времени
    viterbi_time = run_viterbi()

    # 2. Сравнение траекторий
    compare_trajectories()

    # 3. Вывод времени выполнения
    print(f"Общее время выполнения: {viterbi_time:.2f} секунд")
