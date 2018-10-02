import random

def my_hashing_algorithm(a, b):
    return a**b%(a*b)


class server:
    id_and_code = {}

    @classmethod
    def register_id(self, r_id):
        challenge_code = random.randint(1, 1000)
        self.id_and_code[r_id] = challenge_code
        print("サーバがチャレンジコードを送信する")
        return challenge_code
    
    @classmethod
    def called(self, r_id, hash_num):
        challenge_code = self.id_and_code[r_id]
        if my_hashing_algorithm(r_id, challenge_code) == hash_num :
            return "success!"
        else:
            return "faild..."


class client:
    def __init__(self, testserver):
        self.server = testserver
        self.r_id = random.randint(1000, 10000)
        print("クライアントがidを送信する")
        challenge_code = self.server.register_id(self.r_id)
        self.hash_num = my_hashing_algorithm(self.r_id, challenge_code)

    def access(self):
        print("クライアントがハッシュ値を送信する")
        res = self.server.called(self.r_id, self.hash_num)
        print(res)


if __name__ == "__main__":
    testserver = server()
    testclient = client(server)
    testclient.access()

