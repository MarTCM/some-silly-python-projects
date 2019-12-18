import os
import time
import getpass

while True:
    os.system("cls")
    user = "MarTCM"
    passw = "martcm"
    input_user = input("\u001b[32;1mUsername:\u001b[37m")
    if input_user == user:
        input_pass = getpass.getpass('\u001b[32;1mPassword:\u001b[37m')
        if input_pass == passw:
            os.system('python main.py')
            break
        else:
            print("\u001b[31mPassword is incorrect!\u001b[37m")
            time.sleep(1)

    else:
        print("\u001b[31mUsername is incorrect!\u001b[37m")
        time.sleep(1)
