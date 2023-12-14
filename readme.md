# Your Desktop Reminders
    #### Video Demo:  removed
    #### Description:
    Task Manager that lets you create tasks, view tasks, delete tasks and send you an email notification when a task is created, deleted or due.

## Screenshot
<img src="https://github.com/David-Okello/CS50P-Final-Project/blob/main/Screenshot.png" />

## Overview

Your Desktop Reminders is a simple desktop application that allows you to manage your tasks efficiently. It provides features such as creating, viewing, and deleting tasks, along with email notifications for task updates. The project is organized into two main files:

1. **project.py**: Contains the core functionality of the reminder application.
2. **test_project.py**: Includes unit tests for validating the functionality of the project.

## Usage

### 1. project.py

#### 1.1 Classes

- **Task**: Represents a task with properties like name, description, and due date.
  
  - **Methods**:
    - `__init__(self, name, description, due_date=None)`: Initializes the task object.
    - `__str__(self)`: Returns a formatted string representation of the task.

- **Functions**:

  - `rtask(n, d)`: Returns a new Task instance with the provided name and description.
  - `email_alert(body, to)`: Sends an email alert with the specified body to the given email address.
  - `create_task(to_email="test@example.com")`: Creates a new task with user input and sends an email notification.
  - `view_task(name)`: Displays information about a specific task.
  - `delete_task(name, to_email="test@example.com")`: Deletes a task and sends an email notification.
  - `main()`: The main function that serves as the entry point for the application.

#### 1.2 Usage

- Run `main()` to interact with the application.
- Follow the menu options to create, view, or delete tasks.
- Email notifications will be sent for task creation and deletion.

### 2. test_project.py

#### 2.1 Unit Tests

- `test_Task()`: Validates the functionality of the Task class.
- `test_view_task()`: Tests the ability to view an existing task.
- `test_email_alert()`: Verifies the email alert functionality.

#### 2.2 Running Tests

- Use `pytest test_project.py` to execute the unit tests.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/YourDesktopReminders.git
   cd YourDesktopReminders
   ```
2. Install dependancies:

   ```bash
   pip install -r requirements.txt
   ```
3. Create a .env file with the following variables:

   ```bash
   APP_EMAIL=your_email@gmail.com
   APP_PASSWORD=your_email_password
   ```
   Replace your_email@gmail.com and your_email_password with your email credentials.
4. Run the application:

   ```bash
   python project.py
   ```

## Contributing
If you would like to contribute to the project, please follow the Contributing Guidelines.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code for your own purposes.
