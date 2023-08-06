import redis as rds

class UserRegister:
    def __init__(self, user_names, init_nounss=None) -> None:
        self.user_names = user_names
        if init_nounss == None or len(init_nounss) != len(user_names):
            self.init_nounss = [[] for i in range(len(user_names))]
        else:
            self.init_nounss = init_nounss
    
    def register_user(self):
        my_rds = rds.Redis()
        my_rds_pipe = my_rds.pipeline()
        for user_name, init_nouns in zip(self.user_names, self.init_nounss):
            for noun in init_nouns:
                my_rds_pipe.rpush(user_name, noun)

        my_rds_pipe.execute()

class AddNoun:
    def __init__(self, user_name, nouns=[]) -> None:
        self.user_name = user_name
        self.nouns = nouns
    def AddNoun(self):
        my_rds = rds.Redis()
        my_rds_pipe = my_rds.pipeline()
        for noun in self.nouns:
            my_rds_pipe.rpush(self.user_name, noun)
        my_rds_pipe.execute()

