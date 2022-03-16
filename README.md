# Install and run application

## Steps to follow

In order to install the application for development this steps must be followed

### `Clone the repository inside our folder`

For this point you can use a code editor like visual studio code or pycharm and clone the repository using the following link 'https://github.com/ConnorWMcClellan/LionStats.git'

in Visual Studio Code there is an option in the side menu which gives us the option to clone it into our computer and it keeps it conected. 

### `Warning`

Make sure you are not on the master branch, to change branch use git checkout and create a new branch with this format (name.feauture)

### `Create a new virtual enviroment`

After cloning the project, create a virtual enviroment by using the command below. (this is made only the first time you are running the project)

```
python -m venv env
```

"env" is the name we will use for the virtual enviroment.

### `Activate the virtual enviroment`

in order to run and install packages the virtual enviroment must be activated using the command below.

```
env\Scripts\activate
```

we will notice in the terminal that before the location of the project there is a (env) this will tell us we did it correctly
```
(env) C:\Users\Centipede>
```


### `Install Django Framework`

We need to install this framework since we will be working with it. 

```
pip install django
```

### `Run Application`

After creating and installing the packages use the command bellow to navigate the app.
```
python manage.py runserver
```

This is the local link we will access.
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000)

### `!!!IMPORTANT`

After the instalation of a package it must be added to this readme.

### `Instalation`
to install it and create the executable follow the steps in the link bellow.
```
https://github.com/pyinstaller/pyinstaller/wiki/Recipe-Executable-From-Django
```
