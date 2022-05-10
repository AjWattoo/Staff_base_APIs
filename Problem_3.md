# Problem

Create a script that utilizes REST API to upload profile pictures.

## Solution

With the REST API customer ccan upload the profile pictures and this feature is available with the key `avatar` . Make a PUT request to [/users/{userID}](https://developers.staffbase.com/api/api-user#operation/UpdateUser) with the avatar in the data to execute this procedure.

# Procedure

1. All relevant images are stored in one folder and named the pictures with the `lastName` of the user.

2. Customer should get the _userID_ of all the users with REST API [/Users](https://developers.staffbase.com/api/api-user#operation/GetUsers).

3. Get the lasTname of user, match it with the images that were stoted in folder and add that path of image to the `avatar:{{Url}}`.

4. Make put request to _/users/{userID}_ with specific userID and the [avatar data](https://developers.staffbase.com/basic-concepts/avatar-type/#avatar-example) to update the profile image of users.

## Python Script to upload Profile Images

Python script to upload the profile images can be find [here](/uploading_Profile_images.py)
