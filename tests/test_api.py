from api import SampleWeb
import xml.etree.ElementTree as ET
import pytest
from utils import assert_body
from test_data import photo, image64, avatar64
from faker import Faker

api = SampleWeb()

@pytest.mark.parametrize('gender, age', (
                         ('', ''),
                         ('MALE', '1'),
                         ('FEMALE', '23'),
                         ('UNKNOWN', '75')), ids=("Empty gender and age", "Male", "Female", "Unknown"))
def test_get_list_json(gender, age):

    status, result = api.get_list_json(gender, age)

    assert status == 200
    assert "username" in result[0]
    assert "password" in result[0]
    assert "id" in result[0]
    assert "gender" in result[0]
    assert "age" in result[0]

@pytest.mark.parametrize('gender, age', (
                         ('', ''),
                         ('MALE', '1'),
                         ('FEMALE', '23'),
                         ('UNKNOWN', '75')), ids=("Empty gender and age", "Male", "Female", "Unknown"))
def test_get_list_xml(gender, age):

    status, result = api.get_list_xml(gender, age)

    root = ET.fromstring(result)
    users = root.findall('.//username')

    assert status == 200
    assert len(users) > 0

@pytest.mark.parametrize('age, gender, password, username', (
    ('0', 'FEMALE', '1', 'u'),
    ('5', 'MALE', '12345', 'User'),
    ('35', 'UNKNOWN', Faker().password(), Faker().first_name())),
    ids=('1 symbol data', 'Short data', 'Normal data')
)
def test_add_user_with_data(age: int, gender: str, password: str, username):
    status, result = api.create_new_user_with_form_data(age, photo, gender, password, username)

    assert status == 200
    assert_body(age, gender, password, username, result)

@pytest.mark.parametrize('age, gender, password, username',(
                ('3', 'FEMALE', 'p', 'u'),
                ('17', 'MALE', '123', 'user'),
                ('29', 'UNKNOWN', Faker().password(), Faker().first_name()))
)
def test_create_user_by_json(age, gender, password, username):
    status, result = api.create_user_by_json(age, gender, password, username)

    assert status == 200


def test_get_user_by_body(get_id):
    status, result = api.get_user_by_json(get_id)

    assert status == 200
    assert get_id == result['id']

def test_create_user_without_body():
    status, result = api.create_user_without_body()

    assert status == 200
    assert result['age'] == 0
    assert result["gender"] == 'UNKNOWN'
    assert result["password"] == ''
    assert result["username"] == ''


@pytest.mark.parametrize('age, avatar, gender, password, username',(
                ('3', '', 'FEMALE', 'p', 'u'),
                ('17', {'image': open("tests/images/image.jpg", 'rb')}, 'MALE', '123', 'user'),
                ('29', {'avatar': open("tests/images/avatar.jpeg", 'rb')},  'UNKNOWN', Faker().password(), Faker().first_name()))
)
def test_create_user_with_url_encoded(age, avatar, gender, password, username):
    status, result = api.create_user_with_url_encoded(age, avatar, gender, password, username)

    assert status == 200
    assert_body(age, gender, password, username, result)


@pytest.mark.parametrize('age, avatar, gender, password, username',(
                ('0', 'null', 'FEMALE', ' ', ' '),
                ('18', image64, 'MALE', '123', 'user'),
                ('35', avatar64,  'UNKNOWN', Faker().password(), Faker().first_name()))
)
def test_create_user_with_xml(age, avatar, gender, password, username):
    status, result = api.create_user_with_xml(age, avatar, gender, password, username)

    assert status == 200
    assert_body(age, gender, password, username, result)


def test_delete_user_by_id(get_id):
    status, result = api.delete_user_by_id(get_id)

    assert status == 200
    assert "Delete successfully" in result

def test_get_user_by_id(get_id):
    status, result = api.get_user_by_id(get_id)

    assert status == 200

@pytest.mark.parametrize('age',
        ('0', '1', '18', '75', '101'),
    ids=('Ziro year', 'One year', 'Eighteen years', 'Seventy five years', 'One hundred one years'))
def test_update_age_by_id(get_id, age):
    status, result = api.upadate_age(get_id, age)

    assert status == 200
    assert result['age'] == int(age)