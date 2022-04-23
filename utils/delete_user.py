import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/users"

def deactivate_user(user_id, user_data):
    url = "%s/%s/" % (URL, user_id)
    response = requests.delete(url, json=user_data)
    if response.status_code == 204:
        print("Successfully deactive user.")
    else:
        print("Something went wrong while trying to update user.")

def get_user(user_id):
    url = "%s/%s/" % (URL, user_id)
    response = requests.get(url)
    if response.status_code == 200:
        print("User: ")
        pprint(response.json())
        return response.json().get("user")[0]
    else:
        print("Something went wrong while trying to retrieve the user. ")
        return ""


if __name__ == "__main__":
    user_id = input("Type in the user's id: ")
    target_user = get_user(int(user_id))
    if user_id:
        target_user["user_id"] = user_id
    deactivate_user(target_user, user_id)
    option = input("Would you like to see the deactivate user? [y/N]: ")
    if option == "y" or option == "N":
        get_user(user_id)