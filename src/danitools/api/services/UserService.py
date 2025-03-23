import json, os
from danitools.framework.types.UserResponse import UserResponse

class UserService:
    def get_user(self, id, name):
        return UserResponse(id, name)

    def get_users(self):

        # file_path = "data/users.json"
        print(os.path.dirname(__file__))
        print("=====")
        file_path = os.path.join(os.path.dirname(__file__), "../../data/users.json")
        # 파일을 읽기 모드로 열기
        with open(file_path, "r") as file:
            # JSON 데이터 파싱
            data = json.load(file)
        return data
