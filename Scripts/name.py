#!/c/Users/draciel/Anaconda3/python

print(f"The __name__ is: {__name__}")

def main():
    print("I'm running as a script.")

if __name__ == '__main__':
    main()
else:
    print("I'm being imported")
