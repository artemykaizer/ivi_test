import requests
from api_requests.constants import HOST


class CharactersApi:
    def __init__(self, auth):
        self.auth = auth

    def get_characters(self):
        """
        Получает список персонажей
        :return: список result со всеми персонажами
        """
        return requests.get(f"{HOST}/characters", auth=self.auth)

    def get_character(self, name):
        """
        Получает персонаа по имени
        :param name - имя пресонажа
        :return: объект, описывающий персонажа
        """
        t =  requests.get(f"{HOST}/character?name={name}", auth=self.auth)
        return t

    def post_character(self, data):
        """
        Создает персонажа
        :param data - объект с описанием персонажа
        :return: объект, описывающий персонажа
        """
        return requests.post(f"{HOST}/character", json=data, auth=self.auth)

    def put_character(self, data):
        """
        Изменяет персонажа
        :param data - объект с описанием персонажа
        :return: объект, описывающий персонажа
        """
        return requests.put(f"{HOST}/character", json=data, auth=self.auth)

    def delete_character(self, name):
        """
        Удаляет персонажа
        :param name - имя персонажа для удаления
        :return: возвращает фразу %имя_героя% is deleted
        """
        return requests.delete(f"{HOST}/character?name={name}", auth=self.auth)

    def clear_storage(self):
        """
        Очищает коллекцию.
        """
        return requests.post(f"{HOST}/reset", auth=self.auth)