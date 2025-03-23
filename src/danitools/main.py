from danitools.framework.utils.MathUtils import MathUtils
from danitools.api.services.UserService import UserService

def print_users():
    user_service = UserService()
    data = user_service.get_users() 
    print(data)


def main():
    print("This is the main file")
    print(MathUtils.add(1, 2))
    print_users()


# 이 파일을 main으로 실행항면 패키지 루트가 되므로 from danitools 이 경로가 맞지 않아 오류가 발생합니다. 
# main() 함수 실행은 src/app.py에서 실행해야 함 
if __name__ == "__main__":
    print("This is the main file")