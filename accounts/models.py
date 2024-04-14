from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
# Create your custom user models 
# 1->create user model 
# 2->tell user we are using which usermanager
# objects = UserManger()
# 3->tell django that we are using custom user not default 
# AUTH_USER_MODELS = 'accounts.User'

class UserManger(BaseUserManager):
# BaseUserManager-> allows us to edit way user and superuser is created
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('User Must have an email add')
        if not username:
            raise ValueError('User must have an username')
        user = self.model(
            email = self.normalize_email(email), # normalize -> converts upper to lowercase
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password) #set_password encodes pwd to store in db
        user.save(using=self._db) #using -> which db the manager should user of operations(default db in setting.py->DATABASES)
        return user 
    
    def create_suepruser(self,first_name,last_name,username,email,password=None):
        user = self.create_user(
            email = self.normalize_email(email), # normalize -> converts upper to lowercase
            username = username,
            password= password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin=True
        user.is_active = True 
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    # AbstractBaseUser - >full control inc. auth for users
    # AbstractUser -> only add fields
    RESTAURANT = 1
    CUSTOMER =2
    ROLE_CHOICE=(
        (RESTAURANT,'Restaurant'),
        (CUSTOMER,'Customer'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.CharField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=12,blank =True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE,blank=True,null=True)
    
    #required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # Overridding auth part -> defalut username for login 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    # tell user class which user model we are using (we are using one above)
    objects = UserManger()
    
    def __str__(self):
        return self.email
    
    # return True if active superuser or admin
    def has_perm(self,perm,obj=None):
        return self.is_admin 
    
    def has_module_perms(self,app_label):
        return True


