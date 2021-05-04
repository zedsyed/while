from random import choice

questions = ["Why is the sky red?: ", "Why do people breathe?: ", "Why is there sun?: "]

answer = input(choice(questions)).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()

print("Oh Okay")
