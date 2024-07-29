# class Signup(models.Model):
#     username =models.CharField(max_length=200)
#     email = models.EmailField(max_length=200)
#     password= models.CharField(max_length=200)

#     class Meta:
#         db_table = 'posts_signup'

#     def __str__(self):
#         return self.username

    
# class Role(models.TextChoices):
#     USER = 'user', 'User'
#     ADMIN = 'admin', 'Admin'


# class LogIn(models.Model):
#     username = models.EmailField(max_length=200)
#     password= models.CharField(max_length=200)
#     role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)

#     class Meta:
#         db_table = 'posts_login'

#     def __str__(self):
#         return self.username









# class User(AbstractUser):
#     class Role(models.TextChoices):
#         ADMIN = 'ADMIN','Admin'
#         USER = 'USER','User'

#     base_role = Role.ADMIN

#     role = models.CharField(max_length=50, choices=Role.choices)

#     def save(self,*args, **kwargs):
#         if not self.pk:
#             self.role = self.base_role
#             return super().save(*args,**kwargs)

#         # self.role = self.base_role

# class CustomerManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, *kwargs)
#         return results.filter(role = User.Role.USER)


# class Customer(User):
#     base_role = User.Role.USER

#     user = CustomerManager()

#     class Meta:
#         proxy = True

#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.role = self.base_role
#         super(Customer, self).save(*args, **kwargs)

#     def welcome(self):
#         return "Only for customers"
    
    
# @receiver(post_save, sender=Customer)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.role == 'USER':
#         CustomerProfile.objects.create(user=instance)
    

# class CustomerProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user_id = models.IntegerField(null=True, blank=True)





# class User(AbstractUser):
    # role = models.CharField(max_length=50, choices=ROLES, default="USER")

    # groups = models.ManyToManyField('auth.Group', related_name='posts_user_groups')
    # user_permissions = models.ManyToManyField('auth.Permission', related_name='posts_user_permissions')

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)