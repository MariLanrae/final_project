import unittest

class TestSpaceObjects(unittest.TestCase):

    def setUp(self):
        # Очищаем список перед каждым тестом (если нужно)
        global space_objects
        space_objects = [
            {
                "id": 1,
                "name": "Тестовая Галактика",
                "type": "Галактика",
                "constellation": "Тест",
                "distance_ly": 1000,
                "description": "Тестовый объект."
            }
        ]

    def test_initial_objects_count(self):
        self.assertEqual(len(space_objects), 1)

    def test_add_object_logic(self):
        """Тест: логика добавления объекта (вручную)."""
        new_obj = {
            "id": 2,
            "name": "Новая Звезда",
            "type": "Звезда",
            "constellation": "Лира",
            "distance_ly": 50,
            "description": "Очень яркая."
        }
        space_objects.append(new_obj)
        self.assertEqual(len(space_objects), 2)
        self.assertEqual(space_objects[1]["name"], "Новая Звезда")

if __name__ == '__main__':
    unittest.main()