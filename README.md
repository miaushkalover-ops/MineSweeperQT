# 🧨 Minesweeper (PyQt)

A classic Minesweeper game built with Python and PyQt.  
This project demonstrates GUI development, event-driven programming, and clean object-oriented design.

## 🎮 Gameplay

Minesweeper is a puzzle game where the player uncovers cells on a grid while avoiding hidden mines.

- Left-click to reveal a cell
- Right-click to place or remove a flag
- Numbers indicate nearby mines
- Revealing a mine ends the game
- Revealing all safe cells wins the game

## ✨ Features

- PyQt-based graphical user interface
- Dynamic grid generation
- Configurable board size and mine count
- Recursive opening of empty cells
- Flag system
- Win and lose state detection
- Restart / new game functionality

## 🛠️ Tech Stack

- Python 3
- PyQt (Qt Widgets)
- Object-Oriented Programming
- Event-driven architecture

## 📁 Project Structure

minesweeper/
│

├── assets # Sounds for  gaame

│   ├── boom.wav #🎶
  
│   ├── flag.wav # 🎶

│   ├── shovel.wav # 🎶

├── env # Enviroment

├── Scripts # Seperated python scripts 🐍

│   ├── cell.py # Cell logic

│   ├── decorator.py # Decorator fo different functions

│   ├── dialog.py # Dialog window 

│   ├── game.py # Game logic

│   ├── sound.py # Sound manager

│   ├── styles.py # Css styles

├── main.py # Application entry point



## 🚀 Installation & Run

### Requirements
- Python 3.9+
- PyQt installed

### Install PyQt

### Run the game


## 🎯 Purpose

This project was created to practice:
- Desktop GUI development with PyQt
- Signal-slot communication
- Game logic implementation
- Clean and maintainable code structure

## 🔮 Future Improvements

- Difficulty levels
- Timer and score system
- Sound effects
- Custom themes
- Save and load game state

## 📜 License

MIT License

