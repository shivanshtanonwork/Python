import requests

r = requests.get("https://api.github.com/users/shivanshtanonwork")

# print(r.text)
with open("shivanshtanonwork.txt", "w") as f:
    f.write(r.text)