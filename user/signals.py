from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from datetime import datetime

@receiver(user_signed_up)
def user_signed_up_handler(request, user, **kwargs):
    # Get the user's social account for Google
    socialaccount = user.socialaccount_set.filter(provider='google').first()
    if socialaccount:
        # Get the user's name from the social account's extra data
        name = socialaccount.extra_data.get('name')
        if name:
           user.name=name
        
        
        # birthdate = socialaccount.extra_data
        # print(birthdate)
       
        # if birthdate:
        #     # Set the user's date of birth
        #     user.dateofbirth = datetime.strptime(birthdate, '%Y-%m-%d').date()


        user.save()
