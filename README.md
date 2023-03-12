<p align="center" ><img width="250px" src="https://www.freepnglogos.com/uploads/twitter-logo-png/twitter-logo-vector-png-clipart-1.png"></p>
<h1 align="center">Twitter</h1>

> A Django application looks like Twitter. I created it to practice Django. It does not completely look like Twitter. Not designed fully and doesn't have all functions on Twitter. Also accepted google signup. Django admin panel enabled.



# Setup
1. Clone project `git clone https://github.com/adhnanshereef/twitter.git`
2. Change directory to project folder `cd twitter`
3. Install Virtual Environment `pip install virtualenv`
4. Create Virtual Environment `python -m virtualenv env`
5. Use Virtual Environment `"./env/Scripts/activate"`
6. Install Django `pip install Django`
7. Install Pillow `pip install Pillow`
8. Install alluth essentials for google authentication `pip install django-allauth google-auth google-auth-oauthlib google-auth-httplib2`

>or `pip install Django Pillow django-allauth google-auth google-auth-oauthlib google-auth-httplib2`

9. Make migrations `python manage.py makemigrations`
10. Migrate `python manage.py migrate`
11. Run server `python manage.py runserver`


## Functions
* Signup, Login, Logout
* Edit User
* Tweet
* View Tweets
* Like Tweet
* View Profile
* Follow
* Following and Followers Page
* Signup and Login with Google

### Models
1. User
  > * Name
  > * Username
  > * Email
  > * Website
  > * Bio
  > * Location
  > * Avatar (Profile Picture)
  > * Banner
  > * Date Of Birth
  > * Joined Date
  > * Theme
  > * Following and Followers
  > * Is Online 
  > 
2. Tweet
  > * Id
  > * Content as text
  > * User
  > * Images
  > * Like
  > * Reply
  > * Retweet
  > * Views
  > * Created Date
  > * Updated Date (Currently there is no option to edit tweet)
