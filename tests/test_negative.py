import pytest
from api_requests.characters import CharactersApi
from utils.util import prepare_chacter_data


class TestCharactersNegative():
    def test_get_characters_no_auth(self):
        response = CharactersApi(auth=None).get_characters()
        assert response.status_code == 401, "Некорректный статус код"

    def test_get_character_no_auth(self):
        response = CharactersApi(auth=None).get_character(name="Avalanche")
        assert response.status_code == 401, "Некорректный статус код"

    def test_post_character_no_auth(self):
        character_data = prepare_chacter_data("Unbidden")
        response = CharactersApi(auth=None).post_character(character_data)
        assert response.status_code == 401, "Некорректный статус код"

    def test_put_character_no_auth(self, auth, clear_storage):
        character_data = prepare_chacter_data()
        create = CharactersApi(auth).post_character(character_data)

        assert create.status_code == 200, "Некорректрный статус код при создании"

        edit_character_data = {
            "name": character_data["name"],
            "weight": 359
        }
        response = CharactersApi(auth=None).put_character(edit_character_data)

        assert response.status_code == 401, "Некорректный статус код при изменении персонажа"

    def test_delete_character_no_auth(self, auth, clear_storage):
        character_data = prepare_chacter_data()
        create = CharactersApi(auth).post_character(character_data)

        assert create.status_code == 200, "Некорректрный статус код при создании"

        response = CharactersApi(auth=None).delete_character(name=character_data["name"])

        assert response.status_code == 401, "Некорректный статус код при удалении"

    def test_clear_collection_no_auth(self):
        response = CharactersApi(auth=None).clear_storage()

        assert response.status_code == 401, "Некорректный статус код при удалении"

    def test_create_non_uniq_character(self, auth, clear_storage):
        character_data = prepare_chacter_data("Unbidden")
        CharactersApi(auth).post_character(character_data)
        response = CharactersApi(auth).post_character(character_data)

        assert response.status_code == 400, "Некорректный статус код при создании дубля"

    def test_get_character_no_name(self, auth):
        response = CharactersApi(auth).get_character(name=None)
        assert response.status_code == 400, "Некорректный статус код"

    def test_post_character_incorrect_body(self, auth):
        response = CharactersApi(auth).post_character({})
        assert response.status_code == 400, "Некорректный статус код"

    def test_db_overload(self, auth, clear_storage):
        for char in range(0, 501):
            character_data = prepare_chacter_data()
            CharactersApi(auth).post_character(character_data)

        character_data = prepare_chacter_data()
        response = CharactersApi(auth).post_character(character_data)

        assert response.status_code == 400, "Некорректный статус код"
