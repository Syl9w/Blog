from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='A simple title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.body}', 'Nice body content')
        self.assertEqual(f'{self.post.author}', 'testuser')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/10000/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/' )

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title':"new title", 
            'author':self.user, 
            'body':'some text',
            }
        )
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'new title')
        self.assertContains(response, 'some text')
        self.assertTemplateUsed(response,'post_new.html')
    
    def test_post_update(self):
        response = self.client.post(reverse('post_update',args='1'), {'title':'edited title', 'body':'edited text'})
        self.assertEqual(response.status_code,302)

    def test_post_delete(self):
        response=self.client.get(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code,200)

   
