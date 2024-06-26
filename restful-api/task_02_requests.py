#!/usr/bin/python3
import csv
import requests

def fetch_and_print_posts():
    """
    Fetches all posts from json placeholder and prints their titles.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    
    print(f'Status Code: {response.status_code}')
    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """
    Fetches all posts from json placeholder and saves them to a CSV file.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        data = [{'id': post['id'], 'title': post['title'], 'body': post['body']}
                for post in posts]
        with open('posts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data)
