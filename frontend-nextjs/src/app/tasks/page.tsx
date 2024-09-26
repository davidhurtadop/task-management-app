"use client";

import React from 'react';
import TaskList from '../../components/TaskList';

const TasksPage = () => {
  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        padding: '2rem',
      }}
    >
      <h1>Tasks</h1>
      <TaskList />
    </div>
  );
};

export default TasksPage;
