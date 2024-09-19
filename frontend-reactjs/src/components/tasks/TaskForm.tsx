import { useState } from 'react';
import { Input, Button, Spacer, Text } from '@nextui-org/react';
import api from '../../services/api';
import { Task } from '../../types/task';

interface TaskFormProps {
  onSubmit: (task: Task) => void;
}

const TaskForm: React.FC<TaskFormProps> = ({ onSubmit }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await api.post('/tasks', { title, description });
      onSubmit(response.data); // Pass the created task back to the parent
      setTitle('');
      setDescription('');
    } catch (error) {
      console.error('Error creating task:', error);
      // Handle error (e.g., display an error message)
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <Text h3>Create Task</Text>
      <Input 
        label="Title" 
        value={title} 
        onChange={(e) => setTitle(e.target.value)} 
      />
      <Spacer y={1} />
      <Input 
        label="Description" 
        value={description} 
        onChange={(e) => setDescription(e.target.value)} 
        textArea 
      />
      <Spacer y={1.5} />
      <Button type="submit">Create</Button>
    </form>
  );
};

export default TaskForm;
