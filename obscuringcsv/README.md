# Obscuring CSV

## Statement 
Given a file /tmp/users.csv with the following content:
    
    id,name,surname,identification_number,profession,address,city,state,hobbies 
    1,Peter,Venkman,12345678z,Ghostbuster,14 N Moore St,New York,New York,parapsicology| saving the world
    ...

Write a function in Java, Python or Javascript that renders the information in this file totally anonymous, either by removing or obscuring personal data that could lead to identifying an individual.

## Usage
    $> echo "id,name,surname,identification_number,profession,address,city,state,hobbies\n 1,Peter,Venkman,12345678z,Ghostbuster,14 N Moore St,New York,New York,parapsicology| saving the world" > /tmp/users.csv
    $> python3 obscure_csv.py
    hash('pydoof') gives '18754844497' hash.
