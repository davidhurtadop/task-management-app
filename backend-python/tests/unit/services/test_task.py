import unittest
from unittest.mock import MagicMock, patch
from bson.objectid import ObjectId
from src.services.task import TaskService
from src.models.task import Task
from src.utils.exceptions import NotFoundException


class TestTaskService(unittest.TestCase):

    def setUp(self):
        """Setup method to create a mock MongoDB collection and a TaskService instance 
        before running each test.
        """
        self.mock_collection = MagicMock()
        self.task_service = TaskService(self.mock_collection)

    def test_get_tasks(self):
        """Test case to check if get_tasks method returns a list of tasks."""
        mock_tasks = [
            {'_id': ObjectId(), 'title': 'Task 1', 'description': 'Description 1', 'status': 'Pending', 'user_id': ObjectId()},
            {'_id': ObjectId(), 'title': 'Task 2', 'description': 'Description 2', 'status': 'In Progress', 'user_id': ObjectId()}
        ]
        self.mock_collection.find.return_value = mock_tasks
        tasks = self.task_service.get_tasks()
        self.assertTrue(isinstance(tasks, list))
        self.assertEqual(len(tasks), 2)

    @patch('src.services.task.Task')
    def test_create_task(self, MockTask):
        """Test case to check if create_task method successfully inserts a new task."""
        mock_task_data = {'title': 'Task 1', 'description': 'Description 1', 'status': 'Pending', 'user_id': ObjectId()}
        mock_task_obj = MagicMock(spec=Task)
        MockTask.return_value = mock_task_obj
        self.task_service.create_task(mock_task_data)
        mock_task_obj.save.assert_called_once()

    def test_get_task_found(self):
        """Test case to check if get_task method returns a task when it exists."""
        mock_task = {'_id': ObjectId(), 'title': 'Task 1', 'description': 'Description 1', 'status': 'Pending', 'user_id': ObjectId()}
        self.mock_collection.find_one.return_value = mock_task
        task = self.task_service.get_task(str(mock_task['_id']))
        self.assertEqual(task['title'], 'Task 1')

    def test_get_task_not_found(self):
        """Test case to check if get_task method raises NotFoundException when task doesn't exist."""
        self.mock_collection.find_one.return_value = None
        with self.assertRaises(NotFoundException):
            self.task_service.get_task('non_existent_id')

    @patch('src.services.task.Task')
    def test_update_task_found(self, MockTask):
        """Test case to check if update_task method successfully updates an existing task."""
        mock_task = {'_id': ObjectId(), 'title': 'Task 1', 'description': 'Description 1', 'status': 'Pending', 'user_id': ObjectId()}
        self.mock_collection.find_one.return_value = mock_task
        mock_task_obj = MagicMock(spec=Task)
        MockTask.return_value = mock_task_obj
        updated_data = {'title': 'Updated Task', 'description': 'Updated Description'}
        updated_task = self.task_service.update_task(str(mock_task['_id']), updated_data)
        self.assertEqual(updated_task.title, 'Updated Task')
        self.assertEqual(updated_task.description, 'Updated Description')
        mock_task_obj.save.assert_called_once()

    def test_update_task_not_found(self):
        """Test case to check if update_task method raises NotFoundException when task doesn't exist."""
        self.mock_collection.find_one.return_value = None
        with self.assertRaises(NotFoundException):
            self.task_service.update_task('non_existent_id', {})

    def test_delete_task_found(self):
        """Test case to check if delete_task method successfully deletes an existing task."""
        mock_task_id = ObjectId()
        self.mock_collection.delete_one.return_value.deleted_count = 1
        result = self.task_service.delete_task(str(mock_task_id))
        self.assertTrue(result)

    def test_delete_task_not_found(self):
        """Test case to check if delete_task method returns False when task doesn't exist."""
        mock_task_id = ObjectId()
        self.mock_collection.delete_one.return_value.deleted_count = 0
        result = self.task_service.delete_task(str(mock_task_id))
        self.assertFalse(result)
