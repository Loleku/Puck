import socket

print("\n''Puck'' Original Port Knocking program made by Tomasz ''Loleku'' Zając (https://github.com/Loleku)")

try: 
    UDP_IP = input("\nProvide the IP that you want to knock at: ")
    send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("Type in the range of ports that you want to knock at")
    lowend = int(input("From: "))
    highend = int(input("To: "))

    ways = abs(int(input("How many combinations do you want to print the process for? If you don't want to print any, input 0: ")))
    if ways == 0:
        print("The process won't be printed.")

    counter = 1030302

    if __name__ == '__main__':
        for p1 in range(lowend, highend + 1):
            for p2 in range(lowend, highend + 1):
                for p3 in range(lowend, highend + 1):
                    send.sendto(b"knock", (UDP_IP, p1))
                    send.sendto(b"knock", (UDP_IP, p2))
                    send.sendto(b"knock", (UDP_IP, p3))
                    counter -= 1
                    if ways != 0 and counter % ways == 0:
                        print(f"{p1, p2, p3} | {counter}")
    print("All ports in the provided range for the provided host have been knocked. Thanks for using Puck")

except KeyboardInterrupt:
    print("The knocking process was interrupted by the user.")

except ValueError as ve:
    print(f"Incorrect input value. (ValueError: {ve})")
