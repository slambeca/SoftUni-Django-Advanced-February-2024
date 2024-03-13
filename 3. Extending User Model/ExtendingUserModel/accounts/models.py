# from django.contrib.auth import get_user_model
#
# UserModel = get_user_model()
#
#
# class AccountsUserProxy(UserModel):
#     class Meta:
#         proxy = True
#         ordering = ("first_name", )
#
#     @property
#     def greeting(self):
#         return "Hello!"


# print(UserModel.objects.all()) # ordered by PK
# print(AccountsUserProxy.objects.all()) # ordered by "first_name"