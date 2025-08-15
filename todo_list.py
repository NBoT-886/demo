#!/usr/bin/env python3

import json
from datetime import datetime

class TodoList:
    """A simple todo list manager."""
    
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    
    def add_task(self, description):
        """Add a new task to the todo list."""
        task = {
            'id': self.next_id,
            'description': description,
            'completed': False,
            'created_at': datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.next_id += 1
        return task['id']
    
    def complete_task(self, task_id):
        """Mark a task as completed."""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                task['completed_at'] = datetime.now().isoformat()
                return True
        return False
    
    def delete_task(self, task_id):
        """Delete a task from the list."""
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
    
    def list_tasks(self, show_completed=True):
        """List all tasks."""
        if not show_completed:
            return [task for task in self.tasks if not task['completed']]
        return self.tasks
    
    def save_to_file(self, filename='todo.json'):
        """Save todo list to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def load_from_file(self, filename='todo.json'):
        """Load todo list from a JSON file."""
        try:
            with open(filename, 'r') as f:
                self.tasks = json.load(f)
                # Update next_id to avoid conflicts
                if self.tasks:
                    self.next_id = max(task['id'] for task in self.tasks) + 1
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with empty todo list.")

def demo():
    """Demonstrate the TodoList functionality."""
    todo = TodoList()
    
    print("Todo List Demo")
    print("=" * 14)
    
    # Add some tasks
    todo.add_task("Learn Python")
    todo.add_task("Write documentation")
    todo.add_task("Create unit tests")
    
    print("Current tasks:")
    for task in todo.list_tasks():
        status = "✓" if task['completed'] else "○"
        print(f"  {status} [{task['id']}] {task['description']}")
    
    # Complete a task
    todo.complete_task(1)
    print("\nAfter completing task 1:")
    for task in todo.list_tasks():
        status = "✓" if task['completed'] else "○"
        print(f"  {status} [{task['id']}] {task['description']}")

if __name__ == "__main__":
    demo()