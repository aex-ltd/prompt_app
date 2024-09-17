from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, Group, Permission
from django.utils import timezone 

# custom manager class 
class CustomManager(UserManager):
    # create user 
    def create_user(self, email, password, **extra_fields):
        if email is None:
            raise ValueError('Email is required')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    # create superuser 
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
# custom user 
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=60, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='user_groups')
    permissions = models.ManyToManyField(Permission, related_name='user_permissions')
    login_trials = models.IntegerField(default=0)
    last_failed_login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # USERNAME_FIELD = 'email'

    # increment login trials 
    def increment_login_trials(self):
        self.login_trials += 1
        self.last_failed_login = timezone.now()
        self.save()

    # reset login trials 
    def reset_login_trials(self):
        self.login_trials = 0 
        self.last_failed_login = None 
        self.save()

    def __str__(self):
        return self.email 
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'


