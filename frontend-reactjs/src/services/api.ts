// /services/api.ts
import axios from 'axios';
import { useAuth } from '../hooks/useAuth';

const API_URL = 'http://localhost:5000/api';

export const useApi = () => {
  const { token } = useAuth();

  const instance = axios.create({
    baseURL: API_URL,
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return {
    register: (data: any) => axios.post(`${API_URL}/users/register`, data),
    login: (data: any) => axios.post(`${API_URL}/users/login`, data),
    getTasks: () => instance.get(`/tasks`),
    getTask: (taskId: string) => instance.get(`/tasks/${taskId}`),
    getUserTasks: (userId: string) => instance.get(`/tasks/users/${userId}`),
  };
};
