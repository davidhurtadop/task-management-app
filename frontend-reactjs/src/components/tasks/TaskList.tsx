import { useState, useEffect } from 'react';
import useSWR from 'swr';
import { Card, Grid, Text } from '@nextui-org/react';
import api from '../services/api';
import { Task } from '../types/task';

interface TaskListProps {
  userId?: string; // Optional userId to filter tasks
}

const TaskList: React.FC<TaskListProps> = ({ userId }) => {
  const fetcher = (url: string) => api.get(url).then(res => res.data);
  const { data: tasks, error } = useSWR<Task[]>(
    userId ? `/tasks/users/${userId}` : '/tasks',
    fetcher
  );

  if (error) return <Text color="error">Failed to load tasks</Text>;
  if (!tasks) return <Text>Loading tasks...</Text>;

  return (
    <Grid.Container gap={2}>
      {tasks.map((task) => (
        <Grid xs={12} sm={6} md={4} key={task._id}>
          <Card>
            <Card.Header>
              <Text h4>{task.title}</Text>
            </Card.Header>
            <Card.Body>
              <Text>{task.description}</Text>
            </Card.Body>
          </Card>
        </Grid>
      ))}
    </Grid.Container>
  );
};

export default TaskList;
