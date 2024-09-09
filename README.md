# Task Management App

This is a Task Management application that allows users to create, read, update, and delete tasks.

## Technical Requirements

- BackEnd:
  - Python
  - Flask (framework)
- FrontEnd:
  - ReactJs
  - NextJs (framework)
  - NextUI (framework)
- Database:
  - MongoDB
- Google Code Assist:
  - Gemini

## Install

- [nodejs](https://nodejs.org/en)
- [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
- [python](https://www.python.org/downloads/)
- [wsl2](https://learn.microsoft.com/en-us/windows/wsl/install)
- [docker-desktop](https://docs.docker.com/desktop/release-notes/)

## BackEnd

### Run locally

- Locate on the `backend-python/` folder
- update the `.env` with the mongodb uri and db_name
- uncomment the line `COPY .env /app/` in the Dockerfile to be able to access to the mongodb
- run it in a powershell terminal:

  ```bash
  docker build -t task-management-app .
  docker run -it -rm task-manager-app
  # if you want to check the container run: docker run -it -rm task-manager-app bash
  ```

### Run whole app

- Locate on the path where `docker-compose.yaml` file is created and run:

  ```bash
  docker-compose up -d
  ```

- Create the local db and collections using this `backend-python/tests/mongodb/playground.js` file.

## Functional Requirements

- User Authentication and Authorization
  - Users can sign up, log in, and log out.
  - Passwords must be stored securely.
  - Only authenticated users can access the application.
  - Users can only access their own tasks.
- Task Management
  - Users can create, read, update, and delete tasks.
  - Each task should have a title, description, due date, and status (e.g., pending, in-progress, completed).
  - Users can filter and sort tasks by status and due date.
- API Endpoints
  - RESTful API for all CRUD operations on tasks.
  - Endpoints for user authentication (sign up, log in, log out).
- Frontend Interface
  - Web design compatible with modern browsers.
  - Form validation for user input.
  - Clear display of tasks with filtering and sorting options.

### Non-Functional Requirements  

- Security
  - Protect against common vulnerabilities (e.g., SQL injection, XSS, CSRF).
- Scalability
  - Design the application to be horizontally scalable.  
- Maintainability
  - Write clean, modular, and well-documented code.
  - Ensure unit test coverage.

## Implementation Plan

### Week 1: Setup and Authentication

- [ ] Setup project structure and docker infrastructure.
- [ ] Initialize backend and frontend projects.
- [ ] Create automatic build scripts.
- [ ] Implement user authentication and authorization.
- [ ] Create clear README file with instructions to build/execute.

### Week 2: Task Management API

- [ ] Design and implement the Task API (CRUD operations).
- [ ] Set up MongoDB and integrate it with the backend.
- [ ] Implement unit tests for authentication and task management.

### Week 3: Frontend Development

- [ ] Develop the user interface for task management.
- [ ] Implement state management.
- [ ] Integrate the frontend with the backend API.
- [ ] Implement form validation and responsive design.

### Week 4: Testing and Optimization

- [ ] Write integration tests for the backend.
- [ ] Write unit and end-to-end tests for the frontend.
- [ ] Optimize performance and fix any bugs.
- [ ] Conduct a security audit and ensure compliance with non-functional requirements.

## Annex 1: Detailed Functional Requirements

1. User Authentication and Authorization

- Sign Up
  - Users must provide a valid email address and a password.
  - Password must be at least 8 characters long, contain one uppercase letter, one number, and one special character.
- Log In
  - Users must provide a valid email address and password to log in.
  - Implement rate limiting to prevent brute-force attacks.
- Log Out
  - Users can log out from any active session.
- Session Management
  - Implement JWT for session management.
  - Tokens should expire after a certain period (e.g., 1 hour) and refresh tokens should be used for generating new tokens without re-logging in.
- Access Control
  - Ensure that only authenticated users can access the application.
  - Users should only be able to access and manage their own tasks.

1. Task Management

- Create Task
  - Users can create new tasks by providing a title, description, due date, and status.
  - Validate user input to ensure title and due date are provided.
- Read Task
  - Users can view a list of their tasks.
  - Tasks should be displayed with title, description, due date, and status.
  - Implement pagination for task lists.
- Update Task
  - Users can update existing tasks.
  - Ensure that updates are validated and only valid fields are modified.
- Delete Task
  - Users can delete tasks.
  - Prompt users for confirmation before deletion.
- Task Filtering and Sorting
  - Users can filter tasks by status (e.g., pending, in-progress, completed).
  - Users can sort tasks by due date.

1. Notifications

- Due Soon Notifications
  - Notify users via in-app notifications when tasks are due within the next 24 hours.
- Overdue Notifications
  - Notify users via in-app notifications when tasks are overdue.
- Notification Preferences
  - Users can enable or disable notifications.

1. API Endpoints

- Authentication Endpoints
  - POST /api/auth/signup - Register a new user.
  - POST /api/auth/login - Log in a user.
  - POST /api/auth/logout - Log out a user.
- Task Endpoints
  - GET /api/tasks - Retrieve all tasks for the authenticated user.
  - POST /api/tasks - Create a new task.
  - GET /api/tasks/:id - Retrieve a specific task by ID.
  - PUT /api/tasks/:id - Update a specific task by ID.
  - DELETE /api/tasks/:id - Delete a specific task by ID.

1. Frontend Interface

- User Dashboard
  - Display a summary of tasks (e.g., total tasks, tasks due soon, completed tasks).
- Task List
  - Display tasks in a list or grid format.
  - Provide options to filter and sort tasks.
- Task Form
  - Form to create and update tasks with fields for title, description, due date, and status.
  - Validate form inputs to ensure required fields are provided.
- Responsive Design
  - Ensure the application is usable on both desktop and mobile devices.
- Navigation
  - Implement a navigation menu for easy access to different parts of the application (e.g., Dashboard, Tasks, Profile, Settings).
