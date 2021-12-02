import pywhatkit as kit
def main():
    no_to_msg=input("Enter the no.:")
    msg_to_send=input("Enter the msg to send:")
    hr_for_msg=int(input())
    min_for_msg=int(input())
    kit.sendwhatmsg(f"{no_to_msg}",f"{msg_to_send}",hr_for_msg,min_for_msg)
main()    