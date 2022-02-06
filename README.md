# TTRS
KKL evaluation project.

Clone the project. 
Install the requirements by 
pip install -r requirements.txt
      3.   Set up the database named “ttrs”.
      4.   Run the project.



Individual ETS practice file:
tests.py: It consists of the code to fetch all the tourism data from overpass-turbo 
in form of a list of dictionaries.

amenity_data.py: This python file has a function named “query_generator” and works for all the amenities provided in the parameter of the function.
    
Main file and function for the extraction and storage of data: view.py/ get_tourism_data function. 

![Screenshot from 2022-02-07 00-15-53](https://user-images.githubusercontent.com/16497084/152697003-469acd20-4733-4062-a706-832eb58ce60b.png)

![Screenshot from 2022-02-07 00-28-01](https://user-images.githubusercontent.com/16497084/152697113-cd73735c-19a4-4379-89cb-87722465c1c6.png)
Sc:Sign-in
![Screenshot from 2022-02-07 00-28-07](https://user-images.githubusercontent.com/16497084/152697114-84d4249e-3e65-4c41-a875-2388aa945134.png)
Sc:Register
![Screenshot from 2022-02-07 00-28-59](https://user-images.githubusercontent.com/16497084/152697116-bab4b878-8fad-4e9d-a731-b91e770efcb8.png)
Sc: Dashboard for admin
Refresh Table: It runs get_tourism_data which extracts the data from overpass-turbo to the database.

Display Table: It shows the data stored on the database. The table can be queried with the help of a category.

![Screenshot from 2022-02-07 00-29-08](https://user-images.githubusercontent.com/16497084/152697119-9db71331-748f-4490-b819-e6b5cfa2a797.png)
Sc: List of fetched data
![Screenshot from 2022-02-07 00-30-23](https://user-images.githubusercontent.com/16497084/152697120-99c80d9c-7426-44c7-a320-91fadd21b426.png)
Sc: Database
