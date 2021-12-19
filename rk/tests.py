import unittest
from main import drivers, car_parks, dr_car_park
from main import first_task, second_task, third_task

one_to_many = [(dr.fio, dr.sal, c_p.name) 
    for c_p in car_parks 
    for dr in drivers 
    if dr.car_park_id == c_p.id]
    
many_to_many_temp = [(c_p.name, d_c_p.car_park_id, d_c_p.driver_id) 
    for c_p in car_parks 
    for d_c_p in dr_car_park 
    if c_p.id == d_c_p.car_park_id]
    
many_to_many = [(dr.fio, dr.sal, c_p_name) 
    for c_p_name, _, driver_id in many_to_many_temp
    for dr in drivers if dr.id == driver_id]

class Tests(unittest.TestCase):

    def test_first_task(self):
        self.assertEqual(first_task(car_parks, one_to_many), [('Автопарк №1', ['Петров', 'Базаров']),
         ('Автопарк №2', ['Иванов']), ('Автопарк №3', ['Сидоров', 'Михайлов'])])

    def test_second_task(self):
        self.assertEqual(second_task(car_parks, one_to_many), [('Автопарк №1', 31000), 
         ('Автопарк №3', 30000), ('Автопарк №2', 27000)])

    def test_third_task(self):
        self.assertEqual(third_task(many_to_many), [('Петров', 'Автопарк №1'), 
        ('Иванов', 'Автопарк №2'), ('Михайлов', 'Автопарк №2'), ('Сидоров', 'Автопарк №3'),
         ('Базаров', 'Автопарк №3'), ('Петров', 'Парк №1'), ('Иванов', 'Парк №2'),
          ('Михайлов', 'Парк №2'), ('Сидоров', 'Парк №3'), ('Базаров', 'Парк №3')])


if __name__ == '__main__':
    unittest.main()