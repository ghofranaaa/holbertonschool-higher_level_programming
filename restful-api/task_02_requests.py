#!/usr/bin/python3
import json
import requests


def fetch_and_print():
    """
    Fetches all posts from json placeholder
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    
    print(f'Status Code: {response.status.code}')
    if response.status.code == 200:
        posts = response.json()

    for post in posts:
        print(post['title'])

def fetch_and_save_posts():
    """
    Fetches all posts from json placeholder and saves them to a CSV file.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status.code == 200:
        posts = response.json()
        data = [{'id': post['id'], 'title': post['title'], 'body': post['body']}
                for post in posts]
        with open('post.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id'm 'title', 'body'])
            writer.writeheader()
            writer.writerows(data)
