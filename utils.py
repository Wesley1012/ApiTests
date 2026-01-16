

def assert_body(age, gender, password, username, result):
    assert result['age'] == int(age)
    assert result["gender"] == gender
    assert result["password"] == password
    assert result["username"] == username