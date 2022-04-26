import requests


URL = "http://127.0.0.1:5000/users/"

def deactivate_user(user_id):
    
    response = requests.delete(URL+str(user_id))
    if response.status_code == 204:
        print("Successfully deactive user.")
    else:
        print("Something went wrong while trying to deactivate user.")


if __name__ == "__main__":
    user_id = input("Type in the user's id: ")
    deactivate_user(user_id) 