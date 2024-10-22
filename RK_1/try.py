from multiprocessing import Pool
import time 
class AssemblyMachine:
    def __init__(self, machine_id: int, component_type: str, assembly_time: float, total_components: int):
        self.machine_id = machine_id
        self.component_type = component_type
        self.assembly_time = assembly_time
        self.total_components = total_components
        self.total_time = 0.0

    def assemble(self, component_number: int):
        component = f"{self.component_type}_компонент_{component_number}"
        print(f"Машина {self.machine_id} собрала {component}.")
        return component

    def start_production(self):
        components = []
        for i in range(1, self.total_components + 1):
            component = self.assemble(i)
            components.append(component)
            time.sleep(self.assembly_time)  
        
        total_time = self.assembly_time * self.total_components
        print(f"Машина {self.machine_id} завершила сборку {self.total_components} компонентов за {total_time:.2f} секунд.")
        return components, total_time


class Factory:
    def __init__(self):
        self.machines = []
        self.final_machine = None

    def add_machine(self, machine):
        self.machines.append(machine)

    def set_final_machine(self, final_machine):
        self.final_machine = final_machine

    def _help_to_use_machine(self, machine):
        """Запускаем производство на машине."""
        return machine.start_production()

    def start_production(self):
        if not self.machines:
            print("Нет машин для запуска производства.")
            return

        if not self.final_machine:
            print("Не установлена финальная машина для сборки.")
            return

        # Используем Pool для параллельного запуска сборки на всех машинах
        with Pool(processes=len(self.machines)) as pool:
            # Запускаем производство на всех машинах и собираем результаты параллельно
            results = pool.map(self._help_to_use_machine, self.machines)

        # После завершения работы всех машин запускается финальная сборка
        assembly_times = [result[1] for result in results]  # Времена сборки всех машин
        self.final_machine.assemble_final_product(self.machines, assembly_times)  # Передаем список машин


class FinalAssemblyMachine:
    def __init__(self, machine_id: int):
        self.machine_id = machine_id

    def _help_to_components(self, machine):
        components, _ = machine.start_production()  # Получаем компоненты от машины
        return components

    def assemble_final_product(self, machines, assembly_times):
        all_components = []  # Список для хранения компонентов от всех машин
        
        for machine in machines:
            components = self._help_to_components(machine)
            all_components.append(components)  # Добавляем список компонентов от текущей машины

        print(f"Финальная машина {self.machine_id} собирает финальный продукт из {sum(len(c) for c in all_components)} компонентов.")
        
        total_assembly_time = max(assembly_times)  # Общее время сборки от всех машин
        print(f"Финальная машина {self.machine_id} завершила сборку финального продукта за {total_assembly_time:.2f} секунд.")
    
        # Красивый вывод списка компонентов
        print("Итого список деталей:")
        for i, components in enumerate(all_components):
            print(f"  Машина {i + 1}: {', '.join(components)}")  # Форматированный вывод для каждой машины

        return all_components  # Возвращаем список списков компонентов


# Пример использования
if __name__ == "__main__":
    factory = Factory()

    # Машины собирают компоненты
    machine1 = AssemblyMachine(machine_id=1, component_type="Тип A", assembly_time=0.5, total_components=5)
    machine2 = AssemblyMachine(machine_id=2, component_type="Тип B", assembly_time=1, total_components=4)
    machine3 = AssemblyMachine(machine_id=3, component_type="Тип С", assembly_time=1.5, total_components=6)
    machine4 = AssemblyMachine(machine_id=4, component_type="Тип Д", assembly_time=2, total_components=2)

    factory.add_machine(machine1)
    factory.add_machine(machine2)
    factory.add_machine(machine3)
    factory.add_machine(machine4)

    # Финальная машина
    final_machine = FinalAssemblyMachine(5)
    factory.set_final_machine(final_machine)

    # Начало производства
    factory.start_production()
