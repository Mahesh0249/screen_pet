# screen_pet
# Koko — The Ultimate Desktop Monkey Companion 🐒

Koko (also known as Gremsworth) is an intelligent, interactive, and highly agentic virtual desktop pet built in Python with Tkinter. More than just a distraction, Koko actively monitors your system, helps you focus, and even chats with you!

## 🌟 Core Features

### 1. Interactive Physics & Animations
Koko lives directly on your desktop window:
- **Free Roam:** He walks, scales walls, and falls with gravity physics.
- **Dynamic Floor:** Enable "Toggle Window Perch" and Koko will use your open application windows as physical platforms to stand on.
- **Interactive Mouse:** Enable "Follow Mouse" and he will chase your cursor around the screen.
- **Drag & Drop:** You can click and hold Koko to pick him up and throw him anywhere on your screen.

### 2. Productivity Assistant ⏱️
Koko makes sure you get your work done:
- **Focus Mode (Pomodoro):** Start a 25-minute focus session. Koko will hold a book and look busy. If you get distracted by websites like Twitter or YouTube, he will yell at you!
- **Time Tracker:** Log your hours! Start a project, and Koko will silently log how many minutes you've worked on it, providing a summary when you're done.
- **Interactive To-Do List:** Add tasks via the menu. If you are idle for too long, Koko might pop up and remind you about your first pending task.
- **Hydration & Posture Coach:** If Koko notices you've been working too long, he'll remind you to sit up straight and drink water.

### 3. PC System Monitoring 🖥️
Koko keeps an eye on your computer's health:
- **CPU/RAM Panic:** If your CPU or Memory usage spikes above 80-85%, Koko will warn you!
- **Battery Warning:** If your laptop battery drops below 15%, Koko gets shocked and begs to be plugged in.
- **Internet Status:** If you lose Wi-Fi connection, Koko will let you know you're stranded.
- **Git Nagging:** If you are inside a Git repository and haven't committed in over an hour, Koko will aggressively remind you to commit your code!
- **Desktop Trash Cleaning:** Koko monitors your desktop. If it has too many files, he'll complain. You can also ask him to physically clean your PC's temporary `Temp` files to save space!

### 4. 💬 Chat with Koko (Agentic Features)
You can converse with Koko by right-clicking him and selecting **"💬 Chat with Koko"**. He understands various commands and natural language inputs:

#### Greetings & Small Talk
*   **"hello", "hi", "hey", "hola", "sup", "what's up"**: Koko will reply with a randomized, fun greeting.
*   **"good morning"**: Koko wishes you a good morning and asks for bananas. 🌅
*   **"good afternoon"**: Koko wishes you a sunny afternoon. ☀️
*   **"good evening"**: Koko asks if you're working late. 🌙
*   **"good night"**: Koko immediately puts himself to sleep! 💤
*   **"how are you"**: Koko expresses his eagerness to work.
*   **"time"** / **"what time is it"**: Koko will check your system and tell you the exact current time. ⏰
*   **"joke"**: Koko tells a monkey-related pun.
*   **"are you working"**: Koko confirms he's always on the job. 💻

#### Action Commands (Agentic Control)
*   **"open notepad"**: Koko physically launches Windows Notepad for you.
*   **"dance"**: Triggers Koko's happy dance animation.
*   **"sleep"**: Forces Koko to take a nap right where he is.
*   **"focus"**: Automatically starts the 25-minute Pomodoro Focus Mode.
*   **"fetch"**: Koko drops a tennis ball on your screen that you can throw around for him to chase and catch!
*   **"plant"** / **"seed"**: Koko drops a little seed on the ground! Over time (every 30 seconds), it will autonomously grow into a beautiful flower.
*   **"clean"**: Koko aggressively hunts down temporary files and deletes them to free up PC storage.
*   **"clean ram"** / **"free ram"**: Koko uses Windows APIs to forcefully trim inactive memory from running processes, optimizing your PC's active RAM!

## 🛠️ How to Run
Make sure you have Python installed, along with `psutil`.

```bash
pip install psutil
python gremsworth.py
```
