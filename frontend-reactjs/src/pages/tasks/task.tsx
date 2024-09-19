// /pages/tasks.tsx
import { useEffect, useState } from 'react';
import { useApi } from '../../services/api';

export default function TasksPage() {
  const [tasks, setTasks] = useState([]);
  const { getTasks } = useApi();

  useEffect(() => {
    async function fetchTasks() {
      try {
        const { data } = await getTasks();
        setTasks(data);
      } catch (err) {
        console.error('Failed to load tasks');
      }
    }

    fetchTasks();
  }, []);

  return (
    <div className="container mx-auto py-10">
      <h1 className="text-2xl font-bold">Tasks</h1>
      <ul>
        {tasks.map((task: any) => (
          <li key={task.id}>{task.title}</li>
        ))}
      </ul>
    </div>
  );
}
