class Users:
    def __init__(
        self, user_name, user_home, user_local, user_email, user_password
    ):

        self.user_name = user_name
        self.user_home = user_home
        self.user_local = user_local
        self.user_email = user_email
        self.user_passwrod = user_password


Alpha_Prime = Users(
    'Rene Pessoto', 'Jundiaí', 'Casa', 'rene.pessoto@gmail.com', 'senha-teste'
)

if __name__ == '__main__':
    ...
