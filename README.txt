STAPPEN OM HET PROJECT TE MAKEN!!

1: django-admin.py startproject mysite.

2:  2.1: mysite --> settings.py --> timezone = Europe/Berlin  
    2.2:  STATIC_ROOT = os.path.join(BASE_DIR, 'static') onder STATIC_URL
3: Create db: python manage.py migrate

4: Starting server: python manage.py runserver

5: Nieuwe app maken: python manage.py startapp appname

6: Creating a model: appname/models.py --> add code (classes/props/methods)

7: Prepare migration file: python manage.py makemigrations appname

8: Apply to db: python manage.py migrate appname

9:  9.1: Open appname/admin.py
    9.2: Import the last made model like: from .models import Modelname
    9.3: add this line of code: admin.site.register(Modelname)

10: Check if admin working: go to: http://127.0.0.1:8000/admin/

11: 11.1: Make a superuser: in console: python manage.py createsuperuser
    11.2: Enter username/E-mail/password

12: Log in at http://127.0.0.1:8000/admin/

13: Try out your model in admin page

14: Creating URL's 

15: 15.1: Open mysite/urls.py
    15.2: Some quick regex cheat sheet:
            ^ = for the beginning of the text
            $ = for the end of the text
            \d = for a digit
            +  = to indicate that the previous item should be repeated at least once
            () = to capture part of the pattern
        
    15.3: include the appname url, add: url(r'', include('appname.urls')),
          And add from: django.conf.urls import include,url

    15.4 create a new file appname/urls.py

    15.5 import:    from django.conf.urls import url
                    from . import views

    15.6 add urlpatterns: example: 
             urlpatterns = [ url(r'^$', views.post_list, name='post_list'), ]
             Here is post_list the view which maps on the url with regex ^$.

16: create views in appname/views.py example:
        def post_list(request):
            return render(request, 'blog/post_list.html', {})

17: create template directory in appname directory, in the tempalte directory create another directory.
    In this directory create a html file with the name you've given in the urlpatter(in example view.post_list, so post_list.html.

18: 18.1: in appname/views.py, add from .models import modelName
    18.2: Create a QuerySet variable, example: posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    18.3: The last parameter in render() are things the template should use. In this case the queryset variable, so add for example: {'post' : posts}
          QuerySet info: https://docs.djangoproject.com/en/1.9/ref/models/querysets/

19: Display the data: you posts variable in the view.py will return a list.
    To go through the list you will have to use a for loop in your template: Example: 

        {% for post in posts %}
            <div>
                <p>published: {{ post.published_date }}</p>
                <h1><a href="">{{ post.title }}</a></h1>
                <p>{{ post.text|linebreaksbr }}</p>
            </div>
        {% endfor %}

    In this example we can get each attribute of post defined in the model. we can also pipe the data through a filter like |linebreakbr

20: Extending template (to use a template on multiple parts of the website)
    Create a base.html template in the template/blog directory. This template will be used on every page!
    for exampe: put all your html in the base.html and within the body add:

        {% block content %}
        {% endblock %

    This is a block, and within the block will be code inserted from another file
    Now create a 2nd html file and add the actual code in it: for example 

        {% block content %}
            {% for post in posts %}
                <div class="post">
                    <div class="date">
                        {{ post.published_date }}
                    </div>
                    <h1><a href="">{{ post.title }}</a></h1>
                    <p>{{ post.text|linebreaksbr }}</p>
                </div>
            {% endfor %}
        {% endblock %}

    Notice starting with {% block content %} and ending with {% endblock %} and the code in between. 
    Now we only have to connect the 2 templates: 
    Add this line of code to the file you just created: {% extends 'blog/base.html' %}


21. Completion of the very simple website! Next steps will extend it based on the djangoGirlTutorial!

1: add this in your post_list.html:  <h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
    blog.views.post_detail is a path to a post_detail view we want to create. 
    Please note: blog is the name of our application (the directory blog), views is from the name of the views.py file and the last bit – post_detail – is the name of the view.

    Now we have to make a url and view for post_detail!
    
