import unittest
from unittest.mock import MagicMock, patch
from app.models import Item


class TestStaticCode(unittest.TestCase):
    def test_item_model_repr(self):
        """Test the __repr__ method of the Item model."""
        item = Item(id=1, name="Test Item", description="Test Description")
        self.assertEqual(repr(item), "<Item Test Item>")

    def test_item_creation_logic(self):
        """Test creating an item instance (logic-only, no database)."""
        item = Item(name="Test Item", description="Test Description")
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.description, "Test Description")

    @patch("app.models.Item")
    def test_query_all_items(self, mock_item_class):
        """Test querying all items with a fully mocked Item class."""
        # Mock the `all()` method
        mock_item_class.query.all.return_value = [
            Item(id=1, name="Item 1", description="Description 1"),
            Item(id=2, name="Item 2", description="Description 2"),
        ]

        # Simulate the query
        items = mock_item_class.query.all()
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0].name, "Item 1")
        self.assertEqual(items[1].description, "Description 2")

    @patch("app.models.Item")
    def test_query_single_item(self, mock_item_class):
        """Test querying a single item with a fully mocked Item class."""
        # Mock the `get()` method
        mock_item_class.query.get.return_value = Item(id=1, name="Item 1", description="Description 1")

        # Simulate the query
        item = mock_item_class.query.get(1)
        self.assertEqual(item.name, "Item 1")
        self.assertEqual(item.description, "Description 1")


if __name__ == "__main__":
    unittest.main()

