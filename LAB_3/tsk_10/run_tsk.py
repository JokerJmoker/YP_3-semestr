import subprocess

# Выполнение первой команды
subprocess.run(['python', 'generate_viterbi_trajectory.py', 'graph.ldj', 'localization_config.json', 'output.json'], check=True)

# Выполнение второй команды
subprocess.run(['python', 'correspond_trajectories.py', 'true_trajectory.json', 'output.json'], check=True)
