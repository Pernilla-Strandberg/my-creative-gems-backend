from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='pernilla', password='pass')

    def test_list_posts(self):
        pernilla = User.objects.get(username='pernilla')
        Post.objects.create(owner=pernilla, title='testing title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_auth_user_can_create_post(self):
        self.client.login(username='pernilla', password='pass')
        response = self.client.post('/posts/', {'title': 'testing title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_not_auth_user_cant_create_post(self):
        response = self.client.post('/posts/', {'title': 'testing title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        pernilla = User.objects.create_user(
            username='pernilla', password='pass')
        anna = User.objects.create_user(username='anna', password='pass')
        Post.objects.create(
            owner=pernilla, title='testing title', content='pernillas content'
        )
        Post.objects.create(
            owner=anna, title='testing another title', content='annas content'
        )

    def test_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'testing title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_own_post(self):
        self.client.login(username='pernilla', password='pass')
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_another_users_post(self):
        self.client.login(username='pernilla', password='pass')
        response = self.client.put('/posts/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
