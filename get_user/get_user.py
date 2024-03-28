import requests

def get_user(user):
    r = requests.get(f'https://api.github.com/users/{user}')
    match r.status_code:
        case 200:
            data = r.json()
            return f"Name: {data['name']}, profile url: {data['html_url']}"
        case 404:
            return "Github profile not found"
        case 403:
            data = r.json()
            return data['message']
        case _:
            return f"Unsupported error code - {r.status_code}"


if __name__ == "__main__":
    print(get_user('torvalds'))
    print(get_user('fdjskljfdskljklfjdsklskldds'))
    print(get_user('torvalds/hovercard'))