// src/services/api.test.ts (or api.spec.ts)

import api from './api'; // Import your api.ts file
import MockAdapter from 'axios-mock-adapter';
import { describe, expect, it, beforeEach, afterEach } from 'vitest';

describe('API Service', () => {
  let mock: MockAdapter;

  beforeEach(() => {
    mock = new MockAdapter(api);
  });

  afterEach(() => {
    mock.restore(); // Restore original axios instance after each test
  });

  it('should fetch tasks successfully', async () => {
    const mockTasks = [
      { id: 1, title: 'Task 1', completed: false },
      { id: 2, title: 'Task 2', completed: true },
    ];
    mock.onGet('/tasks').reply(200, mockTasks);

    const response = await api.get('/tasks');
    expect(response.status).toBe(200);
    expect(response.data).toEqual(mockTasks);
  });

  // Add more tests for other API methods (POST, PUT, DELETE)
  // and different scenarios (error handling, authentication, etc.)
});
