import random
import csv
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Updated categories and users
categories = [
    'Bug', 'Feature', 'Design', 'Testing', 'Documentation',
    'Deployment', 'Research', 'Optimization', 'Maintenance', 'Code Review'
]

priorities = ['Low', 'Medium', 'High']
users = ['Preet', 'Smit', 'Naman', 'Bibhab', 'Aarav']  # Custom names

# Extended task keywords
task_keywords = {
    'Bug': ['fix', 'resolve', 'investigate', 'repair', 'troubleshoot', 'debug'],
    'Feature': ['implement', 'add', 'develop', 'create', 'build', 'integrate'],
    'Design': ['design', 'sketch', 'mockup', 'prototype', 'layout', 'plan'],
    'Testing': ['test', 'verify', 'validate', 'run test cases', 'QA', 'simulate'],
    'Documentation': ['document', 'write guide for', 'create README for', 'explain', 'summarize'],
    'Deployment': ['deploy', 'release', 'launch', 'push to production', 'migrate'],
    'Research': ['research', 'analyze', 'explore', 'study', 'investigate'],
    'Optimization': ['optimize', 'improve', 'refactor', 'enhance performance of', 'speed up'],
    'Maintenance': ['maintain', 'update', 'monitor', 'clean up', 'audit'],
    'Code Review': ['review code for', 'refactor', 'check standards for', 'critique', 'analyze pull request']
}

# Task subject generator
def generate_subject():
    return fake.bs().replace(" ", "_")

# Generate task description and deadline
def generate_task(category):
    action = random.choice(task_keywords[category])
    subject = generate_subject()
    deadline = datetime.now() + timedelta(days=random.randint(1, 21))
    return f"{action.capitalize()} the {subject} before {deadline.strftime('%A')}", deadline

# Generate dataset
def generate_dataset(filename='custom_tasks_dataset.csv', num_tasks=300):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Task', 'Category', 'Priority', 'Deadline', 'Assigned_To', 'Status'])

        for _ in range(num_tasks):
            category = random.choice(categories)
            task_desc, deadline = generate_task(category)
            priority = random.choices(priorities, weights=[2, 3, 5])[0]  # High is more frequent
            assigned_to = random.choice(users)
            status = random.choice(['Pending', 'In Progress', 'Completed'])

            writer.writerow([task_desc, category, priority, deadline.strftime('%Y-%m-%d'), assigned_to, status])

    print(f"✅ Generated {num_tasks} tasks in {filename}")

# Run the generator
generate_dataset(num_tasks=2000)
