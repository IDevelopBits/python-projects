from canvasapi import Canvas
import datetime
import os
from dotenv import load_dotenv

# Add this script to a task scheduler so it can automatically run
# This will eventually use an email or text messaging system instead of the terminal

# Load environment variables from .env file
load_dotenv()

# Retrieve API token and Canvas URL from environment variables
API_URL = os.getenv("API_URL") # institution's Canvas URL
API_TOKEN = os.getenv("CANVAS_API_KEY")

# Initialize the Canvas object
canvas = Canvas(API_URL, API_TOKEN)

# Get the list of courses
def get_courses():
    """Fetch all courses the user is enrolled in."""
    courses = canvas.get_courses(enrollment_state='active')
    return courses

# Get today's date
today = datetime.date.today()

def get_assignments(course):
    # Fetch all assignments in the given course
    assignments = course.get_assignments()
    return assignments

def check_due_today(assignment):
    # Check if an assignment is due today
    due_date = assignment.due_at
    if due_date:
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%dT%H:%M:%SZ")
        if due_date.date() == today:
            return due_date
    return None

def check_submission(assignment):
    # Check if the assignment has been submitted
    submission = assignment.get_submission()
    return submission.workflow_state == 'submitted'

def send_terminal_reminder(course, assignment):
    # Print a reminder for the assignment
    print(f"Reminder: The assignment '{assignment.name}' in course '{course.name}' is due tonight!")

def main():
    courses = get_courses()  # Fetch all active courses
    for course in courses:
        print(f"Checking assignments for course: {course.name}")
        assignments = get_assignments(course)
        for assignment in assignments:
            due_today = check_due_today(assignment)
            if due_today and not check_submission(assignment):
                send_terminal_reminder(course, assignment)

if __name__ == "__main__":
    main()