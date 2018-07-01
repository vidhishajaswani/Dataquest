## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t": "day"}
response=requests.get('https://oauth.reddit.com/r/python/top',headers=headers,params=params)
python_top=response.json()

## 3. Getting the Most Upvoted Post ##

python_top_articles = python_top["data"]["children"]
most_upvoted=""
most_upvotes=0
for each in python_top_articles:
    t=each["data"]
    if t["ups"]>=most_upvotes:
        most_upvoted=t["id"]
        most_upvotes=t["ups"]
    

## 4. Getting Post Comments ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
response = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers=headers)

comments = response.json()

## 5. Getting the Most Upvoted Comment ##

comments_list = comments[1]["data"]["children"]


most_upvoted_comment=""
id_up=0
for each in comments_list:
    temp=each["data"]
    if temp["ups"]>=id_up:
        id_up=temp["ups"]
        most_upvoted_comment=temp["id"]
        

## 6. Upvoting a Comment ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params={"dir":1,"id":"d16y4ry"}
response = requests.post("https://oauth.reddit.com/api/vote", headers=headers,json=params)

status=response.status_code