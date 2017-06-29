# instagram-followers-export
Export your instagram followers for FREE!

Tutorial for Google Chrome

Step 1:
Visit your Instagram page and click "followers", when the modal appears, press CMD + OPTION + I (MAC) or CTR + SHIFT + I (Windos).

Step 2:
Go to the network tab

Step 3:
Scroll down in the modal to load more users

Step 4:
Copy the link that appears in the Network Tab (it's like: https://www.instagram.com/graphql/query/?query_id=XXXXXXXXX&id=XXXXXXXXXX&first=10&after=XXXXXXXXX

Step 5:
Replace this:
https://www.instagram.com/graphql/query/?query_id=XXXXXXXXX&id=XXXXXXXXXX&first=10&after=XXXXXXXXX

Into This (incrementing the `first` parameter to a value above your current followers number):
https://www.instagram.com/graphql/query/?query_id=XXXXXXXXX&id=XXXXXXXXXX&first=10000&after=XXXXXXXXX

Load this link into the browser and download it in the same folder where parse.py is located, save the page with name: `data.json`.

Step 6:
run `python parse.py`

Step 7:
You will have a generated `followers.csv` with all your twitter followers.

