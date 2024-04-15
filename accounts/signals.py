from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import User,UserProfile
# We are using postsave signal as we want to CREATE USER PROFILE AS SOON AS USER IS CREATED 
# 1-># created -> Flag returns True if obj is created 
@receiver(post_save,sender=User)
def post_save_create_profile_reciever(sender,instance,created,**kwargs):
    if created:
        # creates the user profile as soon as the user is created 
        UserProfile.objects.create(user=instance)
        print('user profile is created!!')
    # if we make update then signal should send
    else: 
        try:

            profile = UserProfile.objects.get(user = instance)
            profile.save()
            print('user profile updated!!')
        except:
            # create the user if not exists 
            UserProfile.objects.create(user=instance)
            print('Profile does not exist, but I created one!')
        print('user is updated')


#2->connect reciever to sender
# post_save.connect(post_save_create_profile_reciever,sender=User)
        
# FOR PRE SAVE SYNTAX 
@receiver(pre_save,sender=User)
def pre_save_profile_receiver(sender,instance,**kwargs):
    print(instance.username,"This user is being saved - presignal")
