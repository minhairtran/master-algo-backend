from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from .models import Feedback

# Create your tests here.
User = get_user_model()
class FeedbackTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='user')
        self.userTest = User.objects.create_user(username='test', password='test')
        Feedback.objects.create(content="My first feedback", user=self.user)
        Feedback.objects.create(content="My second feedback", user=self.user)
        Feedback.objects.create(content="Not my feedback", user=self.userTest)
        self.totalFeedbackCount = Feedback.objects.all().count()
    
    # def test_user_created(self):
    #     user = User.objects.get(username="user")
    #     userTest = User.objects.get(username="test")
    #     self.assertEqual(user.username, "user")
    #     self.assertEqual(userTest.username, "test")

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='user')
        return client

    def test_feedback_detail_api_view(self):
        client = self.get_client()
        response = client.get("/api/feedbacks/3/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data.get('id'), 3)

    # def test_feedback_list(self):
    #     client = self.get_client()
    #     response = client.get('/api/feedbacks/')
    #     print(response.json())
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.json()), 3)

    # def test_feedback_create_api_view(self):
    #     request_data = {"content": "This is a new feedback"}
    #     client = self.get_client()
    #     response = client.post('/api/feedbacks/create/', request_data)
    #     self.assertEqual(response.status_code, 201)
    #     response_data = response.json()
    #     new_feedback_id = response_data.get("id")
    #     self.assertEqual(self.totalFeedbackCount + 1, new_feedback_id)

    # def test_feedback_delete_api_view(self):
    #     client = self.get_client()
    #     response = client.delete('/api/feedbacks/1/delete/')
    #     self.assertEqual(response.status_code, 200)
    #     response = client.delete('/api/feedbacks/1/delete/')
    #     self.assertEqual(response.status_code, 404)
    #     response_incorrect_owner = client.delete('/api/feedbacks/3/delete/')
    #     self.assertEqual(response_incorrect_owner.status_code, 401)
    #     response = client.delete('/api/feedbacks/4/delete/')
    #     self.assertEqual(response.status_code, 200)
        
