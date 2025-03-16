import json

def main():
    message = {"greeting": "Hello, World!"}
    print(json.dumps(message))

if __name__ == "__main__":
    main()