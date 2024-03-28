# from unittest.mock import patch

# from get_user import get_user

# def test_get_user():
#     with patch('get_user.requests.get') as mocked_request:
#         mocked_request.return_value.status_code = 200
#         mocked_request.return_value.json.return_value = {'name': 'Linus Torvalds',
#                                            'html_url': 'https://github.com/torvalds'}
#         assert get_user('torvalds') == 'Name: Linus Torvalds, profile url: https://github.com/torvalds'