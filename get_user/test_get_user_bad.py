from get_user import get_user

def test_get_user():
    assert get_user('torvalds') == 'Name: Linus Torvalds, profile url: https://github.com/torvalds'
    assert get_user('fdjskljfdskljklfjdsklskldds') == 'Github profile not found'
    assert get_user('torvalds/hovercard') == 'Unsupported error code - 401'