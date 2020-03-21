## Steps to execute Redisngo

### Enter Redis folder
cd Redis/

### Create and Activate the Python env
python3 -m venv redinsgo
source redinsgo/bin/activate

### Install dependencies
pip install -r requirements.txt

### Run the application
python redisngo.py

## About the project

This project is a Bingo like game made using Redis. All the game is generated.

The game starts generating 50 players and cards (with 15 numbers) for each player. After that, the game starts with a random number, updating cards and score for each player. The game ends when a player reach the score 15.

## Demo Gif

![image info](./demo.gif)