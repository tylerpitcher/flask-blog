# 📖 Flask Blog 📖
[![Pytest-All](https://github.com/tylerpitcher/flask-blog/actions/workflows/pytest.yml/badge.svg)](https://github.com/tylerpitcher/flask-blog/actions/workflows/pytest.yml)
[![Python PEP8](https://github.com/tylerpitcher/flask-blog/actions/workflows/style_check.yml/badge.svg)](https://github.com/tylerpitcher/flask-blog/actions/workflows/style_check.yml) <br />
A blogging site created using flask.

```
├── LICENSE
├── README.md
├── .github
│   ├── workflows
│   │   ├── pytest.yml
│   │   └── style_check.yml
│   └── pull_request_template.md
├── .gitignore
├── blog
│   ├── static 
│   │   ├── css
│   │   │   ├── base.css           ======> Base CSS on all pages
│   │   │   ├── form.css           ======> CSS for all form pages
│   │   │   └── responsive.css     ======> Creates responsive viewing
│   │   ├── images
│   │   │   ├── background.jpeg 
│   │   │   └── index.png       
│   │   └── js
│   │       ├── char_count.js      ======> Character count when creating posts
│   │       ├── delete.js          ======> Delete comments & posts
│   │       ├── dismiss.js         ======> Dismiss alerts
│   │       └── displayChart.js    ======> Create & add bar chart
│   ├── templates
│   │   ├── create.html            ======> Create post html
│   │   ├── form.html              ======> Base form html
│   │   ├── index.html             ======> Homepage html
│   │   ├── login.html             ======> Login html
│   │   ├── nav.html               ======> Navbar html
│   │   ├── post.html              ======> Post html
│   │   ├── profile.html           ======> Profile html
│   │   └── signup.html            ======> Sign up html
│   ├── __init__.py                ======> Initiates application
│   ├── __main__.py                ======> Runs application
│   ├── auth.py                    ======> Handles user auth
│   ├── dashboard.py               ======> Content creator dashboard
│   ├── helpers.py                 ======> Helpers for models.py
│   ├── models.py                  ======> Defines database models
│   └── views.py                   ======> Provides views to user
├── blog_test
│   ├── test_backend
│   │   ├── test_comment.py        ======> Test backend ability to comment
│   │   ├── test_login.py          ======> Test backend ability to login
│   │   ├── test_post.py           ======> Test backend ability to post
│   │   └── test_register.py       ======> Test backend registration
│   ├── test_frontend
│   │   ├── test_front_comment.py  ======> Test frontend ability to comment
│   │   ├── test_front_login.py    ======> Test frontend ability to login
│   │   ├── test_front_post.py     ======> Test frontend ability to post
│   │   └── test_front_register.py ======> Test frontend registration
│   ├── __init__.py
│   └── conftest.py                ======> Configures pytests
└── requirements.txt               ======> Requirements for project
```

## Frontend & Backend Testing 
This project includes all-encompassing frontend & backend tests. \
The tests can be found in <a href="https://github.com/tylerpitcher/flask-blog/tree/main/blog_test">blog_test</a>,
 with frontend tests stored in <a href="https://github.com/tylerpitcher/flask-blog/tree/main/blog_test/test_frontend">/blog_test/front_end</a>
and all backend tests in <a href="https://github.com/tylerpitcher/flask-blog/tree/main/blog_test/test_backend">/blog_test/test_backend</a> <br /> <br />
[![Pytest-All](https://github.com/tylerpitcher/flask-blog/actions/workflows/pytest.yml/badge.svg)](https://github.com/tylerpitcher/flask-blog/actions/workflows/pytest.yml) 

## How to Run
Install libraries with pip3,
```
pip3 install -r requirements.txt
```
Start server,
```
python3 -m blog
```
Open your web browser and go to,
```
http://localhost:8081/
```

## Browse Posts
<img src="https://i.imgur.com/EIWor69.png" height="400" alt="list of posts">

## Post & Add Comments
<img src="https://i.imgur.com/ocSygoE.png" height="400" alt="creating new post">
<img src="https://i.imgur.com/LZJ0R1C.png" height="400" alt="adding comment to post">

## Dashboard
View top-performing posts and analyze reader sentiment.
<img src="https://i.imgur.com/QxF2lIM.png" height="400">

## Supports Mobile Browsers
<img src="https://i.imgur.com/31SsVcW.png" height="400" alt="login page for mobile">
