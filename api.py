import requests
import json

from requests_toolbelt import MultipartEncoder


class SampleWeb:
    def __init__(self):
        self.base_url = 'https://sample-web-service-aut.herokuapp.com'

    def get_list_json(self, gender, age):
        headers = {
            "gender" : gender,
            "age" : age
        }
        response = requests.get(self.base_url+'/api/users/accept-json', headers=headers)
        status = response.status_code
        try:
            result = response.json()
        except:
            result = response.text

        return status, result

    def get_list_xml(self, gender: str, age: int):
        headers = {
            "gender" : gender,
            "age" : age
        }
        response = requests.get(self.base_url+'/api/users/accept-xml', headers=headers)
        status = response.status_code
        try:
            result = response.json()
        except:
            result = response.text

        return status, result



    def create_new_user_with_form_data(self, age: int, avatar: str, gender: str, password: str, username: str):

        data = MultipartEncoder(
            fields={
            "age": age,
            "avatar": avatar,
            "gender": gender,
            "password": password,
            "username": username
        })

        header = {'Content-Type': data.content_type}
        res = requests.post(self.base_url+"/api/users/form-data", data=data, headers=header)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def get_user_by_json(self, id: int):

        data = {
            "id": id,
        }
        headers = {'Content-Type': 'application/json'}
        res = requests.get(self.base_url+"/api/users/json", data=json.dumps(data), headers=headers)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def create_user_by_json(self, age: int, gender: str, password: str, username: str):

        data = {
                "age": age,
                "gender": gender,
                "password": password,
                "username": username
            }

        header = {'Content-Type': 'application/json'}
        res = requests.post(self.base_url + "/api/users/json", data=json.dumps(data), headers=header)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def create_user_without_body(self):
        headers = {'Content-Type': 'application/json'}
        res = requests.post(self.base_url + "/api/users/json/no-body", headers=headers)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def create_user_with_url_encoded(self, age: int, avatar: str, gender: str, password: str, username: str):

        data = {
                "age": age,
                "avatar": avatar,
                "gender": gender,
                "password": password,
                "username": username
            }

        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        res = requests.post(self.base_url + "/api/users/urlencoded", data=data, headers=header)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def create_user_with_xml(self, age: int, avatar: str, gender: str, password: str, username: str ):
        data = f'''
        <User>
            <age>{age}</age>
            <avatar>{avatar}</avatar>
            <gender>{gender}</gender>
            <password>{password}</password>
            <username>{username}</username>
        </User>
        '''

        header = {'Content-Type': 'application/xml'}
        res = requests.post(self.base_url + "/api/users/xml", data=data, headers=header)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def delete_user_by_id(self, id: int):

        header = {'Content-Type': '*/*'}
        res = requests.delete(self.base_url + f"/api/users/{id}", headers=header)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def get_user_by_id(self, id):

        headers = {'Content-Type': '*/*'}
        res = requests.get(self.base_url+f'/api/users/{id}', headers=headers)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def upadate_age(self, id, age):

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'age': age
        }
        res = requests.put(f'{self.base_url}/api/users/{id}', data=data, headers=headers)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text

        return status, result
