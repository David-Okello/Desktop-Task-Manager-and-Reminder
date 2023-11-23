# test_project.py
import pytest
from datetime import date

from project import Task, email_alert, create_task, view_task, delete_task,rtask

def test_Task():
    task = rtask("Dance", "Dance Today")
    #task = task("Dance", "Dance Today", date.today())
    assert str(task) == f"Name: Dance\nDescription: Dance Today\nDue date: {date.today()}"

def test_view_task():
    # Test viewing a task that exists
    task = Task("Test Task", "This is a test task")
    task_name = task.name
    view_task(task_name)

def test_email_alert():
    # Test sending an email alert
    body = "Test email body"
    to_email = "test@example.com"
    result = email_alert(body, to_email)
    assert result == "Email sent successfully!"
