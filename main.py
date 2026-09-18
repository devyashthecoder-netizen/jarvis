import speech_recognition as sr
import pyttsx3
import sounddevice as sd
import wave
import tempfile
import os
import datetime
import webbrowser
import subprocess
import psutil

from openai import OpenAI


# ============================================================
# OPENAI
# ============================================================

client = OpenAI()


# ============================================================
# JARVIS VOICE
# ============================================================

engine = pyttsx3.init()

engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)


def speak(text):
    print("JARVIS:", text)

    engine.say(text)
    engine.runAndWait()


# ============================================================
# AI BRAIN
# ============================================================

def ask_jarvis(question):

    try:

        response = client.responses.create(
            model="gpt-5",
            instructions="""
You are JARVIS, a personal AI assistant.

Personality:
- Intelligent
- Calm
- Helpful
- Slightly witty
- Polite
- Natural
- Keep answers reasonably short because they are spoken aloud.
- Never use emojis.

The user is speaking to you through a voice assistant.
""",
            input=question
        )

        return response.output_text

    except Exception as e:

        print("AI ERROR:", e)

        return "I am having trouble connecting to my AI system."


# ============================================================
# LISTEN
# ============================================================

def listen():

    sample_rate = 16000
    duration = 5

    print("\nListening...")

    try:

        recording = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="int16"
        )

        sd.wait()

    except Exception as e:

        print("MICROPHONE ERROR:", e)

        speak("There is a problem with the microphone.")

        return ""


    # Create temporary WAV file

    temp_file = tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    )

    temp_file.close()


    # Save recording

    with wave.open(temp_file.name, "wb") as wf:

        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)

        wf.writeframes(recording.tobytes())


    recognizer = sr.Recognizer()


    try:

        with sr.AudioFile(temp_file.name) as source:

            audio = recognizer.record(source)


        print("Processing...")


        command = recognizer.recognize_google(audio)


        print("YOU:", command)


        return command.lower()


    except sr.UnknownValueError:

        print("I didn't understand.")

        return ""


    except sr.RequestError:

        speak("I cannot connect to the speech recognition service.")

        return ""


    finally:

        try:
            os.remove(temp_file.name)
        except:
            pass


# ============================================================
# APP LAUNCHER
# ============================================================

def open_app(command):

    apps = {

        "calculator": ("calc.exe", "Calculator"),

        "calc": ("calc.exe", "Calculator"),

        "notepad": ("notepad.exe", "Notepad"),

        "file explorer": ("explorer.exe", "File Explorer"),

        "explorer": ("explorer.exe", "File Explorer"),

        "command prompt": ("cmd.exe", "Command Prompt"),

        "cmd": ("cmd.exe", "Command Prompt"),

        "powershell": ("powershell.exe", "PowerShell")

    }


    for app_name, (app_path, display_name) in apps.items():

        if app_name in command:

            try:

                subprocess.Popen(app_path)

                speak(f"{display_name} is open.")

            except:

                speak(f"I could not open {display_name}.")

            return True


    return False


# ============================================================
# JARVIS COMMANDS
# ============================================================

def execute(command):


    # --------------------------------------------------------
    # APPLICATIONS
    # --------------------------------------------------------

    if open_app(command):

        return True


    # --------------------------------------------------------
    # GREETING
    # --------------------------------------------------------

    if "hello" in command or "hi" in command:

        speak("Hello. I am JARVIS. Systems are online.")


    # --------------------------------------------------------
    # TIME
    # --------------------------------------------------------

    elif "time" in command:

        current_time = datetime.datetime.now().strftime(
            "%I:%M %p"
        )

        speak(
            f"The current time is {current_time}."
        )


    # --------------------------------------------------------
    # DATE
    # --------------------------------------------------------

    elif "date" in command:

        today = datetime.datetime.now().strftime(
            "%A, %d %B %Y"
        )

        speak(
            f"Today is {today}."
        )


    # --------------------------------------------------------
    # BATTERY
    # --------------------------------------------------------

    elif "battery" in command:

        battery = psutil.sensors_battery()


        if battery:

            percent = battery.percent


            if battery.power_plugged:

                speak(
                    f"Battery is at {percent} percent "
                    "and the laptop is charging."
                )

            else:

                speak(
                    f"Battery is at {percent} percent."
                )

        else:

            speak(
                "I cannot access the battery information."
            )


    # --------------------------------------------------------
    # RAM
    # --------------------------------------------------------

    elif "ram" in command or "memory" in command:

        memory = psutil.virtual_memory()


        used = memory.used / (1024 ** 3)

        total = memory.total / (1024 ** 3)


        speak(
            f"You are using {used:.1f} gigabytes "
            f"out of {total:.1f} gigabytes of RAM."
        )


    # --------------------------------------------------------
    # CPU
    # --------------------------------------------------------

    elif "cpu" in command or "processor" in command:

        cpu = psutil.cpu_percent(interval=1)


        speak(
            f"Current CPU usage is {cpu} percent."
        )


    # --------------------------------------------------------
    # SYSTEM INFORMATION
    # --------------------------------------------------------

    elif (
        "system information" in command
        or "system info" in command
    ):

        cpu = psutil.cpu_percent(interval=1)

        memory = psutil.virtual_memory()

        battery = psutil.sensors_battery()


        response = (
            f"CPU usage is {cpu} percent. "
            f"RAM usage is {memory.percent} percent."
        )


        if battery:

            response += (
                f" Battery is at {battery.percent} percent."
            )


        speak(response)


    # --------------------------------------------------------
    # GOOGLE
    # --------------------------------------------------------

    elif "open google" in command:

        webbrowser.open(
            "https://www.google.com"
        )

        speak("Google is open.")


    # --------------------------------------------------------
    # YOUTUBE
    # --------------------------------------------------------

    elif "open youtube" in command:

        webbrowser.open(
            "https://www.youtube.com"
        )

        speak("YouTube is open.")


    # --------------------------------------------------------
    # SEARCH
    # --------------------------------------------------------

    elif "search" in command:

        query = command.replace(
            "search",
            "",
            1
        ).strip()


        if query:

            speak(
                f"Searching for {query}."
            )


            url = (
                "https://www.google.com/search?q="
                + query.replace(" ", "+")
            )


            webbrowser.open(url)


        else:

            speak(
                "What would you like me to search for?"
            )


    # --------------------------------------------------------
    # SHUTDOWN JARVIS
    # --------------------------------------------------------

    elif (
        "shutdown" in command
        or "exit" in command
        or "goodbye" in command
    ):

        speak(
            "Shutting down. Goodbye, Young Master."
        )

        return False


    # --------------------------------------------------------
    # AI
    # --------------------------------------------------------

    else:

        response = ask_jarvis(command)

        speak(response)


    return True


# ============================================================
# MAIN
# ============================================================

def main():

    speak(
        "JARVIS online. "
        "All systems are ready."
    )


    running = True


    while running:

        command = listen()


        if command:

            running = execute(command)


# ============================================================
# START JARVIS
# ============================================================

if __name__ == "__main__":

    main()