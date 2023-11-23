from dotenv import dotenv_values
import smtplib 
from email.message import EmailMessage
import sys
from datetime import datetime, date

secrets = dotenv_values(".env")

all_tasks = {}

class Task():
    def __init__(self, name, description, due_date=None):
        """
        Initializing the class.
        :param name: The name of task created.
        :param description: The new task description.
        :param due_date: The due date of the task. Default value if user provides wrong input == date.today()
        """
        self.name = name
        self.description = description
        self.due_date = due_date if due_date else date.today()

    @property
    def name(self):
        """
        Getter for name
        """
        return self._name
    
    @name.setter
    def name(self, name):
        """
        Setter for name
        :param name: The name of the task
        """
        if name in all_tasks:
            raise ValueError("Task with similar name already exists!")
        self._name = name
    
    @property
    def description(self):
        """
        Getter for description
        """
        return self._description
    
    @description.setter
    def description(self, description):
        """
        Setter for description
        :param description: The description of the task
        """
        if len(description) > 200:
            raise ValueError("Description can not be greater than 200 characters!")
        self._description = description

    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nDue date: {self.due_date}"

def rtask(n,d):
    return Task(n,d)

def email_alert(body, to):
    """
    This function will send an email to the user with the given body.
    :param body: The body of the email.
    :param to: The email address to send the email to. (User will be prompted)
    :return: The success message of attempt to send email
    """
    try:
        email = secrets["APP_EMAIL"]
        pas = secrets["APP_PASSWORD"]

        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = "Your Desktop Reminders"
        msg['to'] = to
        msg['from'] = "YourDesktopReminders@noreply.com"

        # The server we use to send emails, in this case, it will be gmail
        smtp_server = "smtp.gmail.com" 
        port = 587

        # This will start our email server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Note the parentheses here
        server.login(email, pas)
        server.send_message(msg)

        # Lastly, quit the server
        server.quit()
        return "Email sent successfully!"
    except smtplib.SMTPException as e:
        print(f"Email not sent! Error: {e}")


def create_task(to_email="test@example.com"):
    """
    This function will create a new task.
    :param to_email: The email address to send the email to. (User will be prompted)
    :return: The new task created.
    """

    name = input("Task name: ")
    description = input("Task description: ")
    due_date = input("Due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        print("Using Todays date as default.")

    task = Task(name, description, due_date)
    all_tasks[name] = task
    print(email_alert(f"New task created: {task.name}\nDescription: {task.description}\nDue: {task.due_date}", to_email))
    return task

def view_task(name):
    """
    This function will view a task.
    :param name: The name of the task to be viewed.
    """
    if all_tasks:
        if name in all_tasks:
            task = all_tasks[name]
            print("\n")
            print(task)
        else:
            print("Task not found")
    else:
        print("No tasks created yet!") 

def delete_task(name, to_email="test@example.com"):
    """
    This function will delete a task.
    :param name: The name of the task to be deleted.
    :param to_email: The email address to send the email to. (User will be prompted)
    """
    if all_tasks:
        if name in all_tasks:
            task = all_tasks[name]
            del all_tasks[name]
            print(email_alert(f"Deleted Task:\n{task}", to_email))
            print("Task deleted successfully!")
            return True
        else:
            print("Task not found")
            return False
    else:
        print("No tasks created yet!")

def main():
    """
    This is the main function.
    """
    print("Welcome to Your Desktop Reminders!\n")
    
    to_email = input("Enter email to send notifications to: ")

    while True:
        print("\n1. Create a new task")
        print("2. View a task")
        print("3. Delete a task")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1: 
                create_task(to_email)
            case 2:
                print("\n")
                for task in all_tasks:
                    print(task)
                name = input("\nEnter the name of the task you want to view: ")
                view_task(name)  
            case 3:
                print("\n")
                for task in all_tasks:
                    print(task)
                name = input("\nEnter the name of the task you want to delete: ") 
                delete_task(name, to_email)
            case 4:
                sys.exit("Exiting Application...")
            case _  : 
                sys.exit("Invalid Choice.")

if __name__ == "__main__":
    main()