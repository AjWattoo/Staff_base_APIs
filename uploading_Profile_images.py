import requests
import json


def authorization():
    access_token = 'Basic API TOKEN'
    headers = {'Authorization': access_token,
               'Content-Type': 'application/json'}

    return headers


def get_users(headers):

    url = 'https://backend.staffbase.com/api/users'
    staffbase_users = requests.get(url, headers=headers)
    users = json.loads(staffbase_users.text)

    return users


def uploading_profile_images(headers, users):
    '''
    Save images in folder with lastName of user
    In this funtion userID and lastname of each user is taken and match it with the folder having images

    '''
    for i in range(len(users['data'])):
        lastname = users['data'][i]['lastName']
        new_url = 'https://backend.staffbase.com/api/users/' + \
            users['data'][i]['id']

        data = {"avatar": {
            "original": {
                "url": '/Path/to/folder/{}.png'.format(lastname),
                "width": 225,
                "height": 225,
                "size": 4650,
                "format": "png",
                "mimeType": "image/png"
            },
            "icon": {
                "url": '/Path/to/folder//{}.png'.format(lastname),
            },
            "thumb": {

                "url": '/Path/to/folder//{}.png'.format(lastname),
            }
        }
        }
        data = json.dumps(data)
        requests.put(new_url, data=data, headers=headers)
        print('Profile image of user {} uploaded successfully'.format(lastname))


if __name__ == '__main__':
    headers = authorization()
    users = get_users(headers)
    uploading_profile_images(headers, users)
