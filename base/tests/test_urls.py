from django.test import SimpleTestCase
from django.urls import resolve, reverse
from base.views import loginPage, profile, logoutUser, registerPage, home, borrow, return_book, add_book, book_list


class TestUrls(SimpleTestCase):

    def test_login(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginPage)

    def test_profile(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_logout(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutUser)

    def test_register(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, registerPage)

    def test_home(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_borrow(self):
        url = reverse('borrow')
        self.assertEquals(resolve(url).func, borrow)

    def test_return(self):
        url = reverse('return-book')
        self.assertEquals(resolve(url).func, return_book)

    def test_add(self):
        url = reverse('add-book')
        self.assertEquals(resolve(url).func, add_book)

    def test_book_list(self):
        url = reverse('book-list')
        self.assertEquals(resolve(url).func, book_list)
