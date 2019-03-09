## Pthon Facial Recognition System
Facial Recognition System using Python

> This version is tested to work on Ubuntu 18.02 with Python 3.6.7

> For current progress read 'whats-new.txt' 

### Requirement
- Python 3.*
- PIP3
- OpenCV

### Installation of Project

- Create a folder
```sh
$ mkdir <your_folder_name>
```
- Go inside created folder
```sh
$ cd <created_folder>
```
- Make git pull of the whole project
```sh
$ git init .
$ git remote add origin https://github.com/mnbl/facial-recognition.git/
$ git pull origin master
```
- Install pip3
```sh
$ sudo apt-get install python3-pip
```

- Install Requirements
```sh
$ pip3 install -r requirements.txt
```
- To run face recognition training and dataset folders are required. Create emplty folders using: 
```sh
$ mkdir trainer dataset
```

## Run Simple face detect
- To run simple face detecect
```sh
$ python3 run.py
```
## Run Simple face recognition
- To create face dataset
```sh
$ python3 face_dataset.py
```
- To train system with available faces
```sh
$ python3 train_face.py
```
- To finally detect face
```sh
$ python3 recognise_face.py
```