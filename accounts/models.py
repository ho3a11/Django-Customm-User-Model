from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager): #Mange User Model for create user and user_admin
    def create_user(self,email,username,phone,password): # create user   $$$$  # after self arg most send USERNAME_FIELD and other User model field
        if not email:
            raise ValueError('Please Enter your Email')
        if not username:
            raise ValueError('Please Enter your UserName')
        if not phone:
            raise ValueError('Please Enter your Phone Number')
        user = self.model(email=self.normalize_email(email), username=username, phone=phone) #use normalize_email() for exchange uppercase Email word to lowerCase
        user.set_password(password) # use for hash password
        user.save(using=self._db) # use for save on the active database
        return user
    
    def create_superuser(self,email,username,phone,password): #create super User
        user =self.create_user(email,username,phone,password)
        user.is_admin = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone']
    
    objects = UserManager() # Introducing the User model  to UserManager class

    def __str__(self) :
        return self.email
    
    def has_perm(selef, perm, obj=None ):  #use for access users to somthing details
        return True
    
    def has_module_perms(self, app_label): #use for access users see result  queries
        return True
    
    @property
    def is_staff(self): # use for access admin users
        return self.is_admin
    