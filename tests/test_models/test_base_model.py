#!/usr/bin/python3

from models.base_model import BaseModel
import unittest


class test_BaseModel(unittest.TestCase):
    """test for a base model"""

    def setUp(self):
        """creates an instance of BaseModel"""

        self.base = BaseModel()

    def test_updated_time(self):
        """test time update"""

        initial_time = self.base.updated_at
        current_time = self.base.save()
        self.assertNotEqual(initial_time, current_time)

    def test_to_dict(self):
        """test instance in dictionary format"""

        base_dict = self.base.to_dict()

        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict.__class__, "BaseMode")
        self.assertEqual(base_dict["id"], base_dict.id)
        self.assertEqual(base_dict["created_at"],
                         base_dict.created_at.isoformat())
        self.assertEqual(base_dict["updated_at"],
                         base_dict.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
