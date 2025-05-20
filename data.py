import random
import csv
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Categories and custom users
categories = [
    'Bug', 'Feature', 'Design', 'Testing', 'Documentation',
    'Deployment', 'Research', 'Optimization', 'Maintenance', 'Code Review'
]

priorities = ['Low', 'Medium', 'High']
users = ['Preet', 'Smit', 'Naman', 'Bibhab', 'Aarav']

# Simulated user behavior scores
user_behavior = {
    'Preet': round(random.uniform(0.6, 0.95), 2),
    'Smit': round(random.uniform(0.4, 0.9), 2),
    'Naman': round(random.uniform(0.3, 0.85), 2),
    'Bibhab': round(random.uniform(0.5, 0.92), 2),
    'Aarav': round(random.uniform(0.2, 0.75), 2)
}

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
def generate_dataset(filename='task_dataset.csv', num_tasks=1000):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Task', 'Category', 'Priority', 'Deadline', 'Assigned_To', 'User_Behavior_Score', 'Status'])

        for _ in range(num_tasks):
            category = random.choice(categories)
            task_desc, deadline = generate_task(category)
            priority = random.choices(priorities, weights=[2, 3, 5])[0]
            assigned_to = random.choice(users)
            behavior_score = user_behavior[assigned_to]
            status = random.choice(['Pending', 'In Progress', 'Completed'])

            writer.writerow([
                task_desc, category, priority,
                deadline.strftime('%Y-%m-%d'), assigned_to,
                behavior_score, status
            ])

    print(f"✅ Generated {num_tasks} tasks with user behavior in {filename}")

# Run it
generate_dataset(num_tasks=2000)
