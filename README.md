<p align="center">
  <img src="https://latorredev.com/assets/Img/Certifications/Holberton.png" alt="HolbertonBnB logo">
</p>

# HOLBERTON BNB

_This project contains a console that can interpret various commands that will be explained here._

## Content of the project 🚀

This is the beginning of the creation of a AirBnB clone app. In the next months this repository will gonna update the code to finish all the backend and frontend; in this currently project we have a functionally console that can interpret commands, store information and reload that same information from any class instances that is stored in an a JSON file.

### Commands of the console 📋

The console can be used interactively or non-interactively. If you want to use it in the non-interactively form you need to echo the command and add a pipe before the command ./console.py 
```
$echo "all" | ./console.py
(hbnb) all
[]
```
But if you want to run it interactively(that's what we recommend) you need to run the console with the command ./console.py and use one of the next commands

* **quit** -> _Quit the console_
```
(hbnb) quit
```
* **EOF** -> _Quit the console_(ctr-d)
```
(hbnb) EOF
```
* **create** -> _Create a instance of the class and show ths class ID_
```
(hbnb) create BaseModel
24418ad1-bc8b-4f44-86de-2046d0f3c632
```
* **show** -> _Prints the string representation of a instance of a given ID_
```
(hbnb) create BaseModel
d216069b-387e-4a36-93f6-37f0c5f67bc6
(hbnb) show BaseModel d216069b-387e-4a36-93f6-37f0c5f67bc6
[BaseModel] (d216069b-387e-4a36-93f6-37f0c5f67bc6) {'id': 'd216069b-387e-4a36-93f6-37f0c5f67bc6', 'created_at': datetime.datetime(2020, 6, 30, 20, 49, 1, 446914), 'updated_at': datetime.datetime(2020, 6, 30, 20, 49, 1, 446948)}
```
*