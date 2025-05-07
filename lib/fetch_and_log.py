import requests
import json
from datetime import datetime
import os
import sys

# Import generate_log directly
from generate_log import generate_log

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}

def format_post_data(posts):
    log_entries = []
    
    # If posts is not a list (e.g., if it's a single post as a dict), convert it to a list
    if isinstance(posts, dict):
        posts = [posts]
    
    for post in posts:
        log_entries.append(f"Post {post.get('id')}: {post.get('title')}")
    
    return log_entries

def write_posts_to_json(posts, filename=None):
    if filename is None:
        today = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"posts_{today}.json"
    
    with open(filename, "w") as file:
        json.dump(posts, file, indent=2)
    
    print(f"Posts data written to {filename}")
    return filename

if __name__ == "__main__":
    # Fetch posts from JSONPlaceholder API
    api_url = "https://jsonplaceholder.typicode.com/posts"
    posts_data = fetch_data(api_url)
    
    if posts_data:
        # Limit to first 5 posts for demonstration
        first_posts = posts_data[:5] if isinstance(posts_data, list) else posts_data
        
        # Format and log the data
        log_entries = format_post_data(first_posts)
        log_filename = generate_log(log_entries)
        
        # Also save the full JSON data
        json_filename = write_posts_to_json(first_posts)
        
        print(f"Process completed successfully.")
        print(f"- Log file: {log_filename}")
        print(f"- JSON file: {json_filename}")
    else:
        print("No data was fetched. Process terminated.")