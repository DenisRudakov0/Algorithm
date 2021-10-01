def domain_name(url):
    if 'www' in url:
        return url.split('.')[1]
    elif url.count('.') < 2 and ('//' not in url):
        return url.split('.')[0]
    else:
        ur = url.split('//')
        return ur[1].split('.')[0]
