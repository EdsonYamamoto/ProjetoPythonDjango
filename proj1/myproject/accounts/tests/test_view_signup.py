from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import signup
from ..forms import SignUpForm

# Create your tests here.
class SingUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
    
    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)
    
    def test_form_inputs(self):
        '''
        esta view vai conter inputs de csrd, username, email, password 1 e password2
        '''
        self.assertContains(self.response, '<input',5)
        self.assertContains(self.response, 'type="text"',1)
        self.assertContains(self.response, 'type="email"',1)
        self.assertContains(self.response, 'type="password"',2)
        
class SuccessfulSignUpTests(TestCase):
    def setUp(self) :
        url = reverse('signup')
        data = {
            'username':'john',
            'email': 'john@gmail.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url,data)
        self.home_url = reverse('home')
    
    def test_redirection(self):
        '''
        validação de formulario deveria redirecionar para a home page
        '''
        self.assertRedirects(self.response,self.home_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        '''
        cria uma nova requisição para uma pagina qualquer
        o resultado de resposta deve ser agora o usuario  'user' neste contexto
        apos o sucesso de se cadastrar
        '''
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)

class InvalidSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url,{})

    def test_signup_status_code(self):
        '''
        uma submissao invalida de formularia,
        deveria retornar a mesma pagina
        '''
        self.assertEquals(self.response.status_code,200)
        
    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())

    
class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2',]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)