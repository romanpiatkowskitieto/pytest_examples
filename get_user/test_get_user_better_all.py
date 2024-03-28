# import pytest
# from unittest.mock import patch

# from get_user import get_user

# @pytest.mark.parametrize("username, status_code, api_json_output, expected_result",
#                          [('torvalds', 200,
#                            {'name': "Linus Torvalds",
#                             'html_url': 'https://github.com/torvalds'},
#                             "Name: Linus Torvalds, profile url: https://github.com/torvalds",
#                            ),
#                           ('fdjskljfdskljklfjdsklskldds', 404, {}, 'Github profile not found',),
#                           ('something', 403, {'message': 'Error 403 - Unauthorized'}, 'Error 403 - Unauthorized',),
#                           ('torvalds/hovercard', 666, {}, 'Unsupported error code - 666', ),
#                           ],
#                          ids=["normal response - Code 200",
#                               "abnormal response - Code 404 Not found",
#                               "abnormal response - Code 403 not access forbidden",
#                               "abnormal response - Code 666"
#                          ])
# def test_get_user(username, status_code, api_json_output, expected_result):
#     with patch('get_user.requests.get') as mocked_request:
#         mocked_request.return_value.status_code = status_code
#         mocked_request.return_value.json.return_value = api_json_output
#         assert get_user(username) == expected_result