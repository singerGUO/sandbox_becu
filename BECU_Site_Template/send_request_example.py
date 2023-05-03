import requests

REST_URL = "http://20.245.192.233/tasks/list"
HEADERS = {"Authorization": "Bearer 8rLGxB7J4EZkK2qLdQb0aw"}

r = requests.get(REST_URL, headers=HEADERS)

# Add your code to error checking for r.status_code.

task_id = r.json()
print(task_id)
