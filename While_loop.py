while True:
    name = input("enter your name (type 'exit' to stop):")
    if name.lower() == 'exit':
        break
    print(f"hello, {name}!")
    print("loop exited.")