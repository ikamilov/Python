from user import User, Admin

users = User('iska', 'kamil')
users1 = User('rav', 'norboev')
users2 = Admin('islam', 'kamilov')
users2.greet_user()
users2.privilege.show_privileges()
users.describe_user() 
users.increment_login_attempts()
users.increment_login_attempts()
users.increment_login_attempts()
users.greet_user()
users.reset_login_attemts()
users.greet_user()

users1.describe_user()
users1.greet_user() 