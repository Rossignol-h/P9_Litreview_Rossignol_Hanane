
# Project 9 - LitReview

 #### This project is a Web application that :
- Displays reviews of books and articles,
- A user can signup login logout,
- A connected user can follow, unflollow or being followed by others,
- UX/UI created from scratch, theme was minimalist.
- Stack used: HTML, CSS,Vanilla JavaScript, and Django.
- Cleaning code tool : Flake 8.
- My Python version : 3.10.1


## Installation

#### clone repository locally :

```bash
git clone https://github.com/Rossignol-h/P9_Litreview_Rossignol_Hanane.git
```

#### open your terminal at :

```bash
cd P9_LitReview_Rossignol_Hanane
```

#### Create a virtual environment :

```bash
python -m venv env   # on Windows
python3 -m venv env  # on Mac or Linux
```

#### Activate virtual environment :
```bash
env/Script/activate  # on Windows
env/bin/activate     # on Mac or Linux
```

#### Install all dependencies from the file 'requirements.txt' :
```bash
pip install -r requirements.txt
```
#### open your terminal at the root of the app  :

```bash
cd app
```

#### Create and populate the database :
```bash
python manage.py migrate
```

#### Run the server :
```bash
python manage.py runserver
```

## Usage 

#### The previous command will automatically generate a link :
```bash
Starting development server at http://127.0.0.1:8000/  # click on this link
# it will open the app on your default browser
```

#### **Note : The database will automatically populate with some users and posts**
- All the usernames & passwords are in "auth-list.txt" file
- This website is optimized for Edge, Mozilla Firefox and Chrome

## Testing 

#### For generate a Flake 8 report :
```bash
flake8 --format=html --htmldir=flake-report
```

#### Now you have in the new generated flake-report folder an index.html file :

open the file index.html in your default browser

## Author

- Rossignol Hanane 
- Github Profile :octocat: [@Rossignol-h](https://github.com/Rossignol-h)