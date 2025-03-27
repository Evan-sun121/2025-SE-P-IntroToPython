while True:
    face = input("Hello or Goodbye ")
    if "Hello" in face:
        print("Hello", end="")
        print("🙂")

    if "Goodbye" in face:
        print("Goodbye", end="")
        print("🙁")
        break
