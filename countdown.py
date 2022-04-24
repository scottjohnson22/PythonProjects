import time


def convert_hours(hours):
    output = hours * 60 * 60
    return output


def convert_minutes(minutes):
    output = minutes * 60
    return output


def main():
    print("Enter how long the timer should go for: ")
    hours = int(input("How many hours? "))
    minutes = int(input("How many minutes? "))
    seconds = int(input("How many seconds? "))
    seconds += convert_hours(hours)
    seconds += convert_minutes(minutes)
    print("Starting countdown!")
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        seconds -= 1
        time.sleep(1)
    print("Countdown complete!!!")


main()
