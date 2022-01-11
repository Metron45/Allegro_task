This is simple example server program returning repositories of any user on Github. Made due to my recrutation to Allegro.

I wanted to minimase amount of frameworks used but at the same time I wanted to use Django. 
Django as a framework is too large for such program and vast majority of its features including database goes unused. 
I decided to use it nonetheless because I wanted it to be bit more advanced "Hello World" example of Django usage.

### Setting up the enviroment:

Inside the powershell console run command:

`pip install django`

`pip install requests`

### Running the server:

Using console inside the directory containing manage.py. Run the server using:

`python .\manage.py runserver`

After that you can query any user by requesting his username as endpoint. Esample on local machine and my username:

`http://127.0.0.1:8000/metron45/`

### Expanding the project:
- Frontend improvements
Currently my program returns simple HTML file. It is more readable than JSON but also could use additional formating to be more readable.
- Index Page
Currently my program doesn't have any user interface to select user to query on page itself. Program could be expanded by adding it.
- Additional views
Program could be explanded providing additional views. For example quering into specific repositories to see their description or ability to compare favourite languages of multiple users.
