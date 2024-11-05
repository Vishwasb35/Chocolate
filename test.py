import unittest
from database import initialize_db, insert_seasonal_flavor, fetch_seasonal_flavors

class TestChocolateHouseApp(unittest.TestCase):

    def setUp(self):
        initialize_db()

    def test_insert_seasonal_flavor(self):
        insert_seasonal_flavor("Test Flavor", "Test Description", "2024-10-01", "2024-12-31")
        flavors = fetch_seasonal_flavors()
        self.assertGreater(len(flavors), 0)
        self.assertEqual(flavors[0]['name'], "Test Flavor")

    def test_fetch_ingredients(self):
        insert_seasonal_flavor("Mint Chocolate", "A refreshing mint paired with rich chocolate", "2024-11-01", "2024-12-31")
        flavors = fetch_seasonal_flavors()
        self.assertTrue(any(f['name'] == "Mint Chocolate" for f in flavors))

if __name__ == "__main__":
    unittest.main()