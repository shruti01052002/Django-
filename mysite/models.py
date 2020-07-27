from django.db import models



# Create your models here.
# creating table for a model
# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password=None, is_active=True, is_staff=False, is_admin=False):
#         if not email:
#             raise ValueError("User must have an email address")
#         if not password:
#             raise ValueError("User must have a password")
#         user_obj = self.model(
#             email=self.normalize_email(email)
#         )
#         user_obj.set_password(password)
#         user_obj.staff = is_staff
#         user_obj.admin = is_admin
#         user_obj.active = is_active
#         user_obj.save(using=self._db)
#         return user_obj
#
#     def create_staffuser(self, email, password=None):
#         user = self.create_user(
#             email,
#             password=password,
#             is_staff=True
#         )
#         return user
#
#     def create_superuser(self, email, password=None):
#         user = self.create_user(
#             email,
#             password=password,
#             is_staff=True,
#             is_admin=True
#         )
#         return user


# class User(AbstractBaseUser):
#     email = models.EmailField(max_length=255, unique=True)
#     full_name = models.CharField(max_length=255, blank=True, null=True)
#     active = models.BooleanField(default=True)
#     staff = models.BooleanField(default=False)
#     admin = models.BooleanField(default=False)
#     timestamp = models.BooleanField()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     def __str__(self):
#         return self.email

    # def get_full_name(self):
    #     return self.email
    #
    # def get_short_name(self):
    #     return self.email
    #
    # @property
    # def is_staff(self):
    #     return self.staff
    #
    # @property
    # def is_admin(self):
    #     return self.admin
    #
    # @property
    # def is_active(self):
    #     return self.active


# class Profile(models.Model):
#     user = models.OneToOneField(User)


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=196)
    message = models.TextField()

    def __str__(self):
        return self.email
