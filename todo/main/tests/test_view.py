import pytest
from django.test import Client
from django.shortcuts import reverse

TEST_CLIENT = {
    'username': 'TestUser',
    'email': '123@123.ru',
    'password': 'q1w2e3r4TT',
}


TEST_ITEM = 'Тестовый список дел'


@pytest.mark.django_db
def test_create_new_list(client, new_user):
    """
    Проверка вьюхи на создание нового списка дел
    """
    csrf_client = Client(endforce_csrf_checks=True)
    csrf_client.login(
        username=new_user.username, password=TEST_CLIENT['password']
    )
    response = csrf_client.get(reverse('main:create'))

    html = response.content.decode()
    assert '<title>Новый список</title>' in html

    csrf = csrf_client.cookies['csrftoken']
    response = csrf_client.post(
        reverse('main:create'),
        data={
            'name': 'Тестовый список дел',
            'csrfmiddlewaretoken': csrf.value
        })
    url = response.url
    assert response.status_code == 302, response.content.decode()

    response = csrf_client.get(url)
    html = response.content.decode()
    assert TEST_ITEM in html
