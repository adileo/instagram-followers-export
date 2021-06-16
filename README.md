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
Copy the link that appears in the Network Tab, it's like: https://i.instagram.com/api/v1/friendships/XXXXXXXXX/followers/?count=12&max_id=XXXXXXXXX%3D%3D&search_surface=follow_list_page (it will show up in the left side list as `?count=12&max_id=XXXX[...]`). Click on Headers, the link will be after `Request URL:`
Step 5:
Replace this:
https://i.instagram.com/api/v1/friendships/XXXXXXXXX/followers/?count=12&max_id=XXXXXXXXX%3D%3D&search_surface=follow_list_page

Into This (incrementing the `count` parameter to a value above your current followers number):
https://i.instagram.com/api/v1/friendships/XXXXXXXXX/followers/?count=10000&max_id=XXXXXXXXX%3D%3D&search_surface=follow_list_page

Load this link into the browser and download it in the same folder where parse.py is located, save the page with name: `data.json`.

Step 6:
run `python parse.py`

Step 7:
You will have a generated `followers.csv` with all your Instagram followers.

