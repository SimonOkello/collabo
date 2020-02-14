from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password
        """
        if not email:
            raise ValueError('Users must have an email address!')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """Creates and saves a staff user with given email and password"""
        user = self.create_user(
            email,
            password=password
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Creates and saves a superuser with the given email and password"""
        user = self.create_user(
            email,
            password=password
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


#  Hook in the New Manager to our model
class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    # notice the absence of a "Password field", that is built in.

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    def __str__(self):
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        #  The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def  has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.staff

    @property
    def is_admin(self):
        """Is the user an admin member?"""
        return self.admin

    @property
    def is_active(self):
        """Is the user active?"""
        return self.active




class Profile(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    bio = models.TextField()
    profession = models.CharField(max_length=100)
    age = models.CharField(max_length=4)
    gender = models.CharField(max_length=10)
    skills = models.CharField(max_length=200)


class Project(models.Model):
    added_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, related_name="projects")
    title = models.CharField(max_length=100)
    description = models.TextField()
    photos = models.ImageField(null= True, upload_to='screenshots')
    created_on = models.DateField()
    duration = models.CharField(max_length=100)
    client_website = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    client_email = models.CharField(max_length=100)
    project_url = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name="reviews")
    client = models.CharField(max_length=100)
    review_description = models.TextField()
    added_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return self.review_description



