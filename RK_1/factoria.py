from multiprocessing import Pool
import time

class AssemblyMachine:
    def __init__(self, machine_id: int, component_type: str, assembly_time: float, total_components: int):
        self.machine_id = machine_id
        self.component_type = component_type
        self.assembly_time = assembly_time
        self.total_components = total_components

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

class FinalAssemblyMachine:
    def __init__(self, machine_id: int):
        self.machine_id = machine_id

    def assemble_final_product(self, components, assembly_times):
        # объединяем все списки компонентов в один
        all_components = [machine_components for machine_components in components]

        print(f"Финальная машина {self.machine_id} собирает финальный продукт из {len(all_components)} компонентов.")
        
        # вычисляем общее время сборки
        total_assembly_time = max(assembly_times)
        print(f"Финальная машина {self.machine_id} завершила сборку финального продукта за {total_assembly_time:.2f} секунд.")
        

        print("Итого список деталей:")
        for i, components in enumerate(all_components):
            print(f"  Машина {i + 1}: {', '.join(components)}")  # Форматированный вывод для каждой машины

        return all_components 

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
        
        # используем Pool для параллельного запуска сборки на всех машинах
        with Pool(processes=len(self.machines)) as pool:
            # Запускаем производство на всех машинах и собираем список списков произведенных компонентов
            results = pool.map(self._help_to_use_machine, self.machines)

        # после завершения работы всех машин запускается финальная сборка
        components = [result[0] for result in results]
        assembly_times = [result[1] for result in results]  
        self.final_machine.assemble_final_product(components, assembly_times)

if __name__ == "__main__":
    factory = Factory()

    machine1 = AssemblyMachine(machine_id=1, component_type="Тип A", assembly_time=0.5, total_components=5)
    machine2 = AssemblyMachine(machine_id=2, component_type="Тип B", assembly_time=1, total_components=4)
    machine3 = AssemblyMachine(machine_id=3, component_type="Тип C", assembly_time=1.5, total_components=6)
    machine4 = AssemblyMachine(machine_id=4, component_type="Тип D", assembly_time=2, total_components=2)

    factory.add_machine(machine1)
    factory.add_machine(machine2)
    factory.add_machine(machine3)
    factory.add_machine(machine4)

    final_machine = FinalAssemblyMachine(5)
    factory.set_final_machine(final_machine)

    factory.start_production()
