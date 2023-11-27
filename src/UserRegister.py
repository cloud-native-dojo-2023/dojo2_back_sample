import redis as rds

class UserRegister:
    def __init__(self, host, port, user_names, init_nounss=None) -> None:
        self.user_names = user_names
        self.host = host
        self.port = port
        if init_nounss == None or len(init_nounss) != len(user_names):
            self.init_nounss = [[] for i in range(len(user_names))]
        else:
            self.init_nounss = init_nounss
    
    def register_user(self):
        my_rds = rds.Redis(host=self.host, port=self.port)
        my_rds_pipe = my_rds.pipeline()
        for user_name, init_nouns in zip(self.user_names, self.init_nounss):
            for noun in init_nouns:
                my_rds_pipe.rpush(user_name, noun)

        my_rds_pipe.execute()

