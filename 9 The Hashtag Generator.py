def generate_hashtag(s):
    if len(s) == 0:
        return False
    s = '#' + s.title()
    s = s.split()
    s = ''.join(s)
    if len(s) > 140:
        return False
    return s
