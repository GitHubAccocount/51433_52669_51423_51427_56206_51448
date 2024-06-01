import time
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
  wait_time = between(1, 5)

  @task
  def get_books(self):
    self.client.get(url='api/books')