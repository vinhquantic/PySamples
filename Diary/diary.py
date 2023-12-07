#!/usr/bin/env python3

from collections import OrderedDict
import datetime
import os
import sys

from peewee import *

db = SqliteDatabase('diary.db')

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = db

def initialize():
    """Create the database and the table if they don't exist."""
    db.connect()
    db.create_tables([Entry], safe = True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_loop():
    """Show the menu"""
    choice = None

    while choice != 'q':
        clear()
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()
        elif choice != 'q':
            print('\nInvalid selection. Please try again.\n')

def add_entry():
    """Add an entry"""
    print('Enter your entry. Press ctrl+d when finished.')
    data = sys.stdin.read().strip()

    if data:
        if input('Save entry? [Yn] ').lower() != 'n':
            Entry.create(content = data)
            print('Saved successfully!')

def add_entry_1():
    """Add an entry"""
    print('Enter your entry. Press ctrl+d when finished.')
    data = input('Enter your entry ').lower()
    if data != 'n':
        Entry.create(content = data)
        print('Saved successfully!')

def view_entries(search_query = None):
    """View previous entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y- %I:%M:%S%p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('\n\n' + '='*len(timestamp))
        print('n) Next entry')
        print('d) Delete entry')
        print('q) Return to main menu')

        next_action = input('Action: [Ndq] ').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)

def search_entries():
    """Search entries for a string"""
    view_entries(input('Search query: '))

def delete_entry(entry):
    """Delete an entry"""
    if input('Are you sure? [yN] ').lower() == 'y':
        entry.delete_instance()
        print('Entry deleted!')

menu = OrderedDict([
    ('a', add_entry_1),
    ('v', view_entries),
    ('s', search_entries)
])

if __name__ == "__main__":
    initialize()
    menu_loop()