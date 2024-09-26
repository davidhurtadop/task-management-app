"use client";

import React, { useState, useEffect } from 'react';
import { Card, CardBody, CardFooter, Button, Input } from '@nextui-org/react';
import api from '../services/api';

interface Task {
  id: number;
  title: string;
  completed: boolean;
}

const TaskList: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [newTaskTitle, setNewTaskTitle] = useState('');

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      const response = await api.get('/tasks');
      setTasks(response.data);
    } catch (error) {
      console.error('Error fetching tasks:', error);
      // Handle error, e.g., show an error message to the user
    }
  };

  const handleCreateTask = async () => {
    try {
      if (newTaskTitle.trim() !== '') {
        const response = await api.post('/tasks', {
          title: newTaskTitle,
          completed: false,
        });
        setTasks([...tasks, response.data]);
        setNewTaskTitle('');
      }
    } catch (error) {
      console.error('Error creating task:', error);
      // Handle error
    }
  };

  const handleDeleteTask = async (id: number) => {
    try {
      await api.delete(`/tasks/${id}`);
      setTasks(tasks.filter((task) => task.id !== id));
    } catch (error) {
      console.error('Error deleting task:', error);
      // Handle error
    }
  };

  const handleUpdateTask = async (task: Task) => {
    try {
      await api.put(`/tasks/${task.id}`, task);
      fetchTasks(); // Update the task list after updating a task
    } catch (error) {
      console.error('Error updating task:', error);
      // Handle error
    }
  };

  return (
    <div>
      <Input
        type="text"
        placeholder="Add a new task..."
        value={newTaskTitle}
        onChange={(e) => setNewTaskTitle(e.target.value)}
        css={{ marginBottom: '$10' }}
      />
      <Button onClick={handleCreateTask} css={{ marginBottom: '$10' }}>
        Add Task
      </Button>

      {tasks.map((task) => (
        <Card key={task.id} css={{ marginBottom: '$10' }}>
          <CardBody>
            <input
              type="checkbox"
              checked={task.completed}
              onChange={() =>
                handleUpdateTask({ ...task, completed: !task.completed })
              }
            />
            <span style={{ marginLeft: '10px' }}>{task.title}</span>
          </CardBody>
          <CardFooter>
            <Button
              color="danger"
              size="sm"
              onClick={() => handleDeleteTask(task.id)}
            >
              Delete
            </Button>
          </CardFooter>
        </Card>
      ))}
    </div>
  );
};

export default TaskList;
