import unittest, requests

base_url = "https://jsonplaceholder.typicode.com"


class TestAlbumsCreate(unittest.TestCase):

    def test_create(self):
        """Создание пустого альбома"""

        user_id = '2'
        result = requests.post(f'{base_url}/user/{user_id}/albums')
        assert result.status_code == 201
        assert result.json()['userId'] == user_id
        assert result.json()['id'] == 101

    def tearDown(self):
        requests.delete(f'{base_url}/albums/101')


class TestAlbumsDelete(unittest.TestCase):

    def setUp(self):
        requests.post(f'{base_url}/user/2/albums')

    def test_delete(self):
        """Удаление пустого альбома"""

        result = requests.delete(f'{base_url}/albums/101')
        assert result.status_code == 200