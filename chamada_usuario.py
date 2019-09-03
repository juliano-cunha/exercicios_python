# 9.11 pág 272
# 9.12 pág 272
from user_module import User
from desc_user_mod import Admin, Privileges

user_normal = User('juliano admin', 'cunha', '3211-2293', 'julianocunhatrabalho@gmail.com')
user_admin = Privileges('juliano admin', 'cunha', '3211-2293', 'julianocunhatrabalho@gmail.com')

# chamada das instancias do modulo
user_normal.describe_user()
user_admin.show_privileges()

