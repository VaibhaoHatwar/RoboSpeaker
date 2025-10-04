# RoboSpeaker 1.1 💞🤖

**Created by Vaibhao Hatwar**

RoboSpeaker is a beginner-friendly Python project that converts text into speech. Users can input any text, and the program reads it aloud. This project is perfect for learning Python basics, working with libraries, and creating interactive applications.

---

## Features

* Cross-platform: Works on **Windows**, **macOS**, and **Linux**.
* Interactive loop: Speak multiple phrases without restarting.
* Exit gracefully: Type `'q'` to quit with a goodbye message.
* Easy to extend: Supports enhancements like voice selection or saving speech to audio.

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/RoboSpeaker.git
cd RoboSpeaker
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv .venv
# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

> If you are on Windows and `pyttsx3` is not installed, this will install it.

---

## How to Use

```bash
python main.py
```

* Type any text and RoboSpeaker will speak it.
* Type `'q'` to exit.

---

## Requirements

* Python 3.x
* [pyttsx3](https://pypi.org/project/pyttsx3/) (for Windows)
* macOS: Built-in `say` command
* Linux: `espeak` installed

---

## Example

```
Welcome to RoboSpeaker 1.1. Created by Vaibhao
Enter 'q' when you want to exit
Enter what you want me to speak: Hello RoboSpeaker
# The program speaks "Hello RoboSpeaker"
Enter what you want me to speak: q
# Program speaks goodbye message and exits
```

---

## License

This project is **open-source** and free to use.
