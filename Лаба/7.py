class Employee:
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.emp_id = kwargs.get('emp_id')

    def get_info(self):
        return f"Имя: {self.name}, ID: {self.emp_id}"


class Manager(Employee):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.department = kwargs.get('department')

    def manage_project(self, project_name):
        return f"Менеджер {self.name} управляет проектом: {project_name}"


class Technician(Employee):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.specialization = kwargs.get('specialization')

    def perform_maintenance(self):
        return f"Техник {self.name} выполняет техническое обслуживание в области: {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, *args, **kwargs):
        Manager.__init__(self, *args, **kwargs)
        Technician.__init__(self, *args, **kwargs)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        team_info = "Команда:\n"
        for member in self.team:
            team_info += member.get_info() + "\n"
        return team_info


emp1 = Employee(name="Иван Иванов", emp_id=1)
print(emp1.get_info())

mgr = Manager(name="Светлана Петрова", emp_id=2, department="IT")
print(mgr.get_info())
print(mgr.manage_project("Разработка ПО"))

tech = Technician(name="Алексей Смирнов", emp_id=3, specialization="Электроника")
print(tech.get_info())
print(tech.perform_maintenance())

tech_mgr = TechManager(name="Мария Кузнецова", emp_id=4, department="IT", specialization="Системное администрирование")
tech_mgr.add_employee(emp1)
tech_mgr.add_employee(tech)
print(tech_mgr.get_team_info())



