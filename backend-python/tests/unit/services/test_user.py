import unittest
from unittest.mock import MagicMock, patch
from bson.objectid import ObjectId
from src.services.user import UserService
from src.models.user import User
from src.utils.exceptions import NotFoundException


class TestUserService(unittest.TestCase):

    def setUp(self):
        """Setup method to create a mock MongoDB collection and a UserService instance 
        before running each test.
        """
        self.mock_collection = MagicMock()
        self.user_service = UserService(self.mock_collection)

    def test_get_users(self):
        """Test case to check if get_users method returns a list of users."""
        mock_users = [
            {'_id': ObjectId(), 'username': 'user1', 'email': 'user1@example.com', 'password': 'password1'},
            {'_id': ObjectId(), 'username': 'user2', 'email': 'user2@example.com', 'password': 'password2'}
        ]
        self.mock_collection.find.return_value = mock_users
        users = self.user_service.get_users()
        self.assertTrue(isinstance(users, list))
        self.assertEqual(len(users), 2)

    @patch('src.services.user.User')
    def test_create_user(self, MockUser):
        """Test case to check if create_user method successfully inserts a new user."""
        mock_user_data = {'username': 'user1', 'email': 'user1@example.com', 'password': 'password1'}
        mock_user_obj = MagicMock(spec=User)
        MockUser.return_value = mock_user_obj
        self.user_service.create_user(mock_user_data)
        mock_user_obj.save.assert_called_once()

    def test_get_user_found(self):
        """Test case to check if get_user method returns a user when it exists."""
        mock_user = {'_id': ObjectId(), 'username': 'user1', 'email': 'user1@example.com', 'password': 'password1'}
        self.mock_collection.find_one.return_value = mock_user
        user = self.user_service.get_user(str(mock_user['_id']))
        self.assertEqual(user['username'], 'user1')

    def test_get_user_not_found(self):
        """Test case to check if get_user method raises NotFoundException when user doesn't exist."""
        self.mock_collection.find_one.return_value = None
        with self.assertRaises(NotFoundException):
            self.user_service.get_user('non_existent_id')

    @patch('src.services.user.User')
    def test_update_user_found(self, MockUser):
        """Test case to check if update_user method successfully updates an existing user."""
        mock_user = {'_id': ObjectId(), 'username': 'user1', 'email': 'user1@example.com', 'password': 'password1'}
        self.mock_collection.find_one.return_value = mock_user
        mock_user_obj = MagicMock(spec=User)
        MockUser.return_value = mock_user_obj
        updated_data = {'username': 'updated_user', 'email': 'updated_user@example.com'}
        updated_user = self.user_service.update_user(str(mock_user['_id']), updated_data)
        self.assertEqual(updated_user.username, 'updated_user')
        self.assertEqual(updated_user.email, 'updated_user@example.com')
        mock_user_obj.save.assert_called_once()

    def test_update_user_not_found(self):
        """Test case to check if update_user method raises NotFoundException when user doesn't exist."""
        self.mock_collection.find_one.return_value = None
        with self.assertRaises(NotFoundException):
            self.user_service.update_user('non_existent_id', {})

    def test_delete_user_found(self):
        """Test case to check if delete_user method successfully deletes an existing user."""
        mock_user_id = ObjectId()
        self.mock_collection.delete_one.return_value.deleted_count = 1
        result = self.user_service.delete_user(str(mock_user_id))
        self.assertTrue(result)

    def test_delete_user_not_found(self):
        """Test case to check if delete_user method returns False when user doesn't exist."""
        mock_user_id = ObjectId()
        self.mock_collection.delete_one.return_value.deleted_count = 0
        result = self.user_service.delete_user(str(mock_user_id))
        self.assertFalse(result)
