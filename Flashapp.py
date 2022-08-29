1.App.py

From Flask import flask, flash, redirect, url_for, session, logging

From Flask, my_sql database, import My SQL

From wtforms, import Form, String Field, Total Area Field, Password Field, validators

From passlib, hash, import sha256-crypt

app=Flask(__name__)

Articles=articles ( )
@app.route ('/'):
def index():
      return render_template('home.html')

@app.route ('/about'):
def about ():
        return render_template('about.html')

@app.route ('/articles')
def articles ():
        return render_template('articles.html', articles=Articles)

@app.route ('/article/<string:id>')
def article ():
render_template('article.html', id=id)


if __name__=='__main__’:
      app.run(debug=True)


2. home.html

{% extends 'layout.html' %}
{% block body %}
< div class=”jumbotron text-center>
    <h1 >Welcome to FlaskApp</h1>
    <p class="lead">Built on Python framework</p>
</div>
{% endblock %}

3. articles.html

{% extends 'layout.html' %}
{% block body%}
    <h1 >Articles</h1>
    <ul class= "list-group">
      {% for article in articles %}
    <li class= "list-group-item">< a href= "articles/{{articles.id}}">{{articles.title}}</a></li> {% endfor %}
</ul>{% endblock %}


4. Layout.html

<!DOCTYPE html>
<html>
    <head>
      < meta charset="utf-8">
        < title>My FlaskApp</title>
   <link rel="stylesheet" href=https://...></head >
<body >
{% include 'include/_navbar.html' %}
<div class= "container">
 {% blockbody %}{% endblock %}
< /div>
<script src=https://...></>
</body>

</html>

5. Navbar

< nav class="navbar navbar-inverse navbar-fixed-top">
< div class= "container"></div>
<div class="navbar-header"></div><button type="button" class="navbar-toggle collapsed" data-toggle="collapse" >
 <span class ="sr-only">toggle navigation</span>
<span class= "icon-bar">< /span>
<span class= "icon-bar">< /span>
<span class= "icon-bar">< /span>


</button>
<a class="navbar-brand" href="#">My FlaskApp</a>
</div>
<div id="navbar" class="collapse navbar-collapse" >
< ul class="nav navbar-nav>
<li class= "active"><a href="/about" >Home</a></li>
<li ><a href="/about" >About</a></li>
<li ><a href="#contact">Contact</a></li>
<li ><a href="/articles" >Articles</a></li>

</ul>
</div><!---/nav-collapse--->
</div>
</nav>

6. data.py

def Articles ():
       articles=[
      {
        'id': 1,
        'title' : 'Article One' ,
        'body' : 'Lorem ipsum',
        'author' : 'Brad Lamz',
        'create-date' : '18-12-2021'
}, {
        'id': 2,
        'title' : 'Article Two' ,
        'body' : 'Lorem ipsum',
        'author' : 'Brad Lamz',
        'create-date' : '18-12-2021'
},{
        'id': 3,
        'title' : 'Article Three' ,
        'body' : 'Lorem ipsum',
        'author' : 'Light bringer',
        'create-date' : '18-12-2021'
},{ 
        'id': 4,
        'title' : 'Article Four' ,
        'body' : 'Lorem ipsum',
        'author' : 'Tata Nsai',
        'create-date' : '18-12-2021'
}
]

7. article.html

{% extends 'layout.html%}
{% blockbody %}
   < h1>{{id}}</h1>
{% endblock%}