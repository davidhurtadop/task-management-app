import TaskForm from '../../components/TaskForm';
import TaskList from '../../components/TaskList';

const TasksPage: React.FC = () => {
  const handleTaskSubmit = (newTask: Task) => {
    // Update the task list (e.g., using SWR's mutate function)
    // ...
  };

  return (
    <>
      <TaskForm onSubmit={handleTaskSubmit} />
      <TaskList />
    </>
  );
};

export default TasksPage;
