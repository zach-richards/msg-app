import serverInteraction.Server as Server
import serverInteraction.PCClient as PCClient

if __name__ == "__main__":
    Server

    while input != "q":
        input = input("Who'd you like to text? (q to quit): ")

        while input != "b":
            if input != "b":
                PCClient.text(message=input)
            else:
                break
        else:
            break