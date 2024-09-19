import { useRouter } from 'next/router';
import useSWR from 'swr';
import { Card, Text } from '@nextui-org/react';
import api from '../../services/api';
import { Task } from '../../types/task';

const TaskDetailsPage: React.FC = () => {
  const router = useRouter();
  const { taskId } = router.query;

  const fetcher = (url: string) => api.get(url).then(res => res.data);
  const { data: task, error } = useSWR<Task>(
    taskId ? `/tasks/${taskId}` : null,
    fetcher
  );

  if (error) return <Text color="error">Failed to load task</Text>;
  if (!task) return <Text>Loading task...</Text>;

  return (
    <Card>
      <Card.Header>
        <Text h3>{task.title}</Text>
      </Card.Header>
      <Card.Body>
        <Text>{task.description}</Text>
      </Card.Body>
    </Card>
  );
};

export default TaskDetailsPage;
