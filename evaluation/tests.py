from django.test import TestCase
from .models import Supervisors, Student, Coordinator, Department
from datetime import date

class TestDepartment(TestCase):
    def setUp(self):
        self.department = Department(name = 'ComputingSciences')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.department, Department))

    def test_saveDepartment(self):
        self.department.save_department()
        departments = Department.objects.all()
        self.assertTrue(len(departments)>0)

class TestCoordinator(TestCase):    
    def setUp(self):
        self.department = Department(name = 'ComputingSciences')
        self.department.save_department()
        self.coordinator = Coordinator(coordinatorsNumber = 'ksuc123', firstName = 'Fredrick', lastName = 'Mzee', email = 'fred@mzee.com', department = self.department, registrationDate = date(2005,5,12))
        
    def test_instance(self):
        self.assertTrue(isinstance(self.coordinator, Coordinator))     

    def test_saveCoordinator(self):
        self.coordinator.save_coordinator()
        coordinators = Coordinator.objects.all()
        self.assertTrue(len(coordinators)>0)
class TestSupervisor(TestCase):
    def setUp(self):
        self.department = Department(name = 'ComputingSciences')
        self.department.save_department()
        self.coordinator = Coordinator(coordinatorsNumber = 'ksuc123', firstName = 'Fredrick', lastName = 'Mzee', email = 'fred@mzee.com', department = self.department, registrationDate = date(2005,5,12))
        self.coordinator.save_coordinator()
        self.supervisor = Supervisors(supervisorsNumber = "ksus123", firstName = 'Teresa', lastName = "Abuya", email= "teresa@abuya.com", department = self.department, coordinator = self.coordinator, registrationDate = date(2020, 3,12))   
    
    def test_instance(self):
        self.assertTrue(isinstance(self.supervisor, Supervisors))
    
    def test_saveSupervisors(self):
        self.supervisor.save_supervisor()
        supervisors = Supervisors.objects.all()
        self.assertTrue(len(supervisors)>0)
class TestStudents(TestCase):
    def setUp(self):
        self.department = Department(name = 'ComputingSciences')
        self.department.save_department()
        self.coordinator = Coordinator(coordinatorsNumber = 'ksuc123', firstName = 'Fredrick', lastName = 'Mzee', email = 'fred@mzee.com', department = self.department, registrationDate = date(2005,5,12))
        self.coordinator.save_coordinator()
        self.supervisor = Supervisors(supervisorsNumber = "ksus123", firstName = 'Teresa', lastName = "Abuya", email= "teresa@abuya.com", department = self.department, coordinator = self.coordinator, registrationDate = date(2020, 3,12))  
        self.supervisor.save_supervisor() 
        self.student = Student(serialNumber = 'ksust123', firstName = "Benta", lastName = "Njoki", email = 'benta@njoki.com', department = self.department, supervisor = self.supervisor, registrationDate = date(2021,2,12))
    def test_instance(self):
        self.assertTrue(isinstance(self.student, Student))
    def test_students(self):
        self.student.save_students()
        students = Student.objects.all()
        self.assertTrue(len(students)>0)