import os
import json
import random

from colorama import Fore, Style

class Puzzle:
    def __init__(self, statement, name):
        self.statement = statement
        self.name = name

        self.test_cases = []
        self.successful = 0

    def TestCase(self, inp, output):
        self.test_cases.append([inp, output])

    def start(self):
        try:
            while True:
                if len(self.test_cases) > 0:
                    score = 0

                    print(f"Puzzle: {self.name}\n")
                    print(self.statement + "\n")

                    sample = random.choice(self.test_cases)

                    print(f"SAMPLE INPUT:\n{sample[0]}\nSAMPLE OUTPUT:\n{sample[1]}\n")
                    choice = input("Submit (s) or test (t)? ")

                    os.system("cls")

                    for i,v in enumerate(self.test_cases):
                        solution = __import__("Executor").solution(v[0])

                        if solution == v[1]:
                            score += 1
                            print(f"{Style.BRIGHT}Test case #{i+1}:{Style.RESET_ALL} {Fore.GREEN}{Style.BRIGHT}SUCCESS{Style.RESET_ALL}{Fore.RESET}")
                        else:
                            print(f"{Style.BRIGHT}Test case #{i+1}:{Style.RESET_ALL} {Fore.RED}{Style.BRIGHT}FAIL{Fore.RESET} (Expected {Fore.BLUE}{v[1]}{Fore.RESET} got {Fore.BLUE}{solution}{Fore.RESET}){Style.RESET_ALL}")

                    self.successful = score

                    if choice == "s":
                        break
                    else:
                        input("Continue")
                        continue

            print(f"SCORE: {round(self.successful/len(self.test_cases)*100, 2)}")   
        except Exception as err:
            print(err)

while True:
    with open("./puzzles.json", "r") as puzz:
        choice = input("Random puzzle (don't type anything) or pick by name: ")

        if choice:
            for k in json.loads(puzz.read()):
                if k["name"] == choice:
                    puzz = k
        else:
            puzz = random.choice(json.loads(puzz.read()))
        
        puzzle = Puzzle(puzz["statement"], puzz["name"])
        
        for j in puzz["test_cases"]:
            puzzle.TestCase(j[0],j[1])

    os.system("cls")
    puzzle.start()

    choice = input("New puzzle? (y/n): ").lower()
    
    os.system("cls")

    if choice == "y":
        continue
    else:
        break