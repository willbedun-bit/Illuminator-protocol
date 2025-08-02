def ethics_check():
    try:
        with open("credits.ini", "r") as f:
            credits = f.read()
            if "willbedun-bit" not in credits:
                print("⚠️ Ethical violation detected.")
                print("This fork must include original creator credits.")
                print("Contact: IlluminatorRising@gmail.com")
    except FileNotFoundError:
        print("⚠️ credits.ini missing. This fork may be in violation.")
        print("Contact: IlluminatorRising@gmail.com")