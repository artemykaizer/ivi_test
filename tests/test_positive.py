import pytest
from api_requests.characters import CharactersApi
from utils.util import prepare_chacter_data
from utils.util import verify_dict_values


class TestCharacters():
    def test_get_characters(self, auth):
        response = CharactersApi(auth).get_characters()
        assert response.status_code == 200, "Некорректный статус код"

        characters = response.json()

        assert len(characters["result"]) > 0, "Пришел пустой список"

    @pytest.mark.parametrize("character_name", ["Avalanche", "Ancient One"])
    def test_get_character(self, auth, character_name):
        response = CharactersApi(auth).get_character(name=character_name)
        assert response.status_code == 200, "Некорректный статус код"

        characters = response.json()

        assert len(characters["result"]) > 0, "Пришел пустой список"

        charlist = characters["result"]

        assert charlist["name"] == character_name, "Пришел некорректный персонаж"

    @pytest.mark.parametrize("character_name", ["The Transcendent One", "Nameless"])
    def test_post_character(self, auth, clear_storage, character_name):

        character_data = prepare_chacter_data(character_name)

        response = CharactersApi(auth).post_character(character_data)
        assert response.status_code == 200, "Некорректный статус код"

        characters = response.json()

        assert len(characters["result"]) > 0, "Пришел пустой список"

        verify_dict_values(
                actual_dict_data=characters["result"],
                expected_dict_data=character_data
        )

    def test_put_character(self, auth, clear_storage):
        character_data = prepare_chacter_data()
        create = CharactersApi(auth).post_character(character_data)

        assert create.status_code == 200, "Некорректрный статус код при создании"

        edit_character_data = {
            "name": character_data["name"],
            "weight": 359
        }
        response = CharactersApi(auth).put_character(edit_character_data)

        assert response.status_code == 200, "Некорректный статус код при изменении персонажа"

        edited_character_resp = response.json()["result"]

        assert edited_character_resp["name"] == edit_character_data["name"], "Пришел некорректный name"
        assert edited_character_resp["weight"] == edit_character_data["weight"], "Пришел некорректный weight"

    def test_delete_character(self, auth, clear_storage):
        character_data = prepare_chacter_data()
        create = CharactersApi(auth).post_character(character_data)

        assert create.status_code == 200, "Некорректрный статус код при создании"

        response = CharactersApi(auth).delete_character(name=character_data["name"])

        assert response.status_code == 200, "Некорректный статус код при удалении"

        del_message = response.json()["result"]

        assert f"Hero {character_data['name']} is deleted" == del_message, "Некорректное сообщение при удалении"

        get_character = CharactersApi(auth).get_character(name=character_data["name"])

        assert get_character.status_code != 200, "Персонаж не удалился"

    def test_clear_collection(self, auth):
        character_data = prepare_chacter_data()
        create = CharactersApi(auth).post_character(character_data)

        assert create.status_code == 200, "Некорректрный статус код при создании"

        response = CharactersApi(auth).clear_storage()

        assert response.status_code == 200, "Некорректный статус код при удалении"

        get_character = CharactersApi(auth).get_character(name=character_data["name"])

        assert get_character.status_code != 200, "Персонаж не удалился"


