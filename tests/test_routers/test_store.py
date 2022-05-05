import pytest
import unittest


@pytest.mark.usefixtures("app")
class TestStore(unittest.TestCase):
    def setUp(self):
        self.new_store_dict = {"name": "New Store 1"}
        self.existing_store_name = "My Wonderful Store"
        self.non_existing_store_name = "Non-Existing Store"
        self.new_item_dict = {"name": "New Item 1", "price": 14.50}
    
    def tearDown(self):
        pass
    
    def test_create_store(self):
        with self.app.app_context():
            response = self.client.post("/store", json=self.new_store_dict)
            data = response.json
            self.assertEqual(data["newStore"], {'items': [], 'name': self.new_store_dict["name"]})
            self.assertEqual(response.status_code, 200)
            
    def test_get_store_existing(self):
        with self.app.app_context():
            response = self.client.get(f"/store/{self.existing_store_name}")
            data = response.json
            self.assertEqual(data,
                {"store": 
                    {"name": "My Wonderful Store",
                    "items": [
                        {
                            "name": "My Item",
                            "price": 15.99
                        },
                        {
                            "name": "New Item 1",
                            "price": 14.5
                        }
                    ]}
                }
            )
            self.assertEqual(response.status_code, 200)
            
    def test_get_store_non_existing(self):
        with self.app.app_context():
            response = self.client.get(f"/store/{self.non_existing_store_name}")
            data = response.json
            self.assertEqual(data, {"message": "Store not found"})
            self.assertEqual(response.status_code, 404)
        
    def test_get_all_stores(self):
        with self.app.app_context():
            response = self.client.get("stores")
            data = response.json
            self.assertEqual(data, 
                {"stores":
                    [
                        {
                            "name": "My Wonderful Store",
                            "items": [
                                {
                                    "name": "My Item",
                                    "price": 15.99
                                },
                                {
                                    "name": "New Item 1",
                                    "price": 14.5
                                }
                            ]
                        },
                        {
                            "name": "New Store 1",
                            "items": []
                        }
                    ]
                }
            )
            self.assertEqual(response.status_code, 200)
    
    def test_add_item_to_store_existing(self):
        with self.app.app_context():
            response = self.client.post(f"store/{self.existing_store_name}/item", json=self.new_item_dict)
            data = response.json
            self.assertDictEqual(data,
                {"store": 
                    {
                        "items": [
                            {
                                "name": "My Item",
                                "price": 15.99
                            },
                            {
                                "name": "New Item 1",
                                "price": 14.5
                            }
                        ],
                        "name": "My Wonderful Store"
                    }
                }
            )
            self.assertEqual(response.status_code, 200)
            
    def test_add_item_to_store_non_existing(self):
        with self.app.app_context():
            response = self.client.post(f"store/{self.non_existing_store_name}/item", json=self.new_item_dict)
            data = response.json
            self.assertEqual(data, {"message": "Store not found"})
            self.assertEqual(response.status_code, 404)
            
            
    def test_get_items_from_store_existing(self):
        with self.app.app_context():
            response = self.client.get(f"/store/{self.existing_store_name}/items")
            data = response.json
            self.assertEqual(data, 
                {"storeItems":
                    [
                        {
                            "name": "My Item",
                            "price": 15.99
                        },
                        {
                            "name": "New Item 1",
                            "price": 14.5
                        }
                    ]   
                }                                          
            )
    
    def test_get_items_from_store_non_existing(self):
        with self.app.app_context():
            response = self.client.get(f"/store/{self.non_existing_store_name}/items")
            data = response.json
            self.assertEqual(data, {"message": "Store not found"})
            self.assertEqual(response.status_code, 404)
            