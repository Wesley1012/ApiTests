import pytest
from faker import Faker
from api import SampleWeb
from utils import assert_body
import random
api = SampleWeb()


@pytest.fixture(scope='function')
def get_id():

    age = str(random.randint(1, 100))
    gender = random.choices(('MALE', 'FEMALE', 'UNKNOWN'), k=1)[0]
    password = Faker().password()
    username = Faker().first_name()

    status, result = api.create_user_by_json(age, gender, password, username)

    id = result['id']

    assert_body(age, gender, password, username, result)

    yield id

    try:
        status, result = api.delete_user_by_id(id)

        assert status == 200
        assert "Delete successfully" in result
    except:
        print('OK: User has been delete.')
