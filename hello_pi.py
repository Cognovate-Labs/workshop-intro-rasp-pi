import platform
import time
import random
import os

# Welcome Message
print("Hello, Student! 🐧 Welcome to your Raspberry Pi!")
time.sleep(1)

# Fun ASCII Art
print(r"""
   _______________
  |               |
  |   RASPBERRY   |
  |       PI      |
  |_______________|
      \  ^__^
       \ (oo)\_______
         (__)\       )\/\
             ||----w |
             ||     ||
""")
time.sleep(1)

# System Information
print("\nLet's check what your Raspberry Pi is up to:")
print(f"Machine Name: {platform.node()}")
print(f"System: {platform.system()} {platform.release()}")
print(f"Processor: {platform.processor()}")
print(f"Python Version: {platform.python_version()}")
time.sleep(2)

# Interactive Greeting
name = input("\nWhat's your name? ")
print(f"\nHi {name}! I'm your Raspberry Pi. 🍓 Nice to meet you!")
time.sleep(1)

# Random Fun Facts about Raspberry Pi
fun_facts = [
    "Did you know? The Raspberry Pi was originally designed to teach kids to code.",
    "Fun fact: Over 40 million Raspberry Pi units have been sold worldwide!",
    "The Raspberry Pi's GPIO pins can control lights, sensors, and even robots!",
    "Your Raspberry Pi can be turned into a retro gaming console with software like RetroPie!",
    "Cool fact: The Raspberry Pi can run a web server, making it great for small websites.",
]

# Display Fun Facts
print("\n🎉 Here's your Raspberry Pi fun facts!")
for fact in fun_facts:
    print(f"💡 {fact}")
    time.sleep(2)

# Goodbye Message
print("\nThat's it for now. Remember, you can make the Pi do anything you want with Python.")
print("Stay curious and keep experimenting! 🌟\n")
