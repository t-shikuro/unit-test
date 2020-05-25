---
title: "Web Scraping and APIs"
date: 2020-01-30
tags: [md5, hash, ]
header:
  image: "/images/bs4.png"
excerpt: "Bs4"
mathjax: "true"
---

## Overview

A Python script that checks whether your password has ever been hacked using SHA1 Hash. Using https://api.pwnedpasswords.com/range/ and `requests` library. The secure password checker uses [k-anonymity](https://dataprivacylab.org/projects/kanonymity/index.html) by using Python `hashlib` module. The website https://haveibeenpwned.com allows users to check whether their e-mail has ever been leaked from a data breach. Hackers essentially use a dictionary to log-in to websites using massive lists of {username: password}. By creating a secure way to check your password and e-mail by not submitting it online and instead using the password api interacting with this Python script.


INSTALL

> pip3 install requests

TO RUN:
type python3 checkmypass.py [input password] in terminal and returns integer value of how many times the password was found.


TO RUN in Python script

```python
    import requests
    import hashlib
    import sys


    def request_api_data(query_char):
        url = 'https://api.pwnedpasswords.com/range/' + query_char
        res = requests.get(url)
        if res.status_code != 200:
            raise RuntimeError(
                f'Error fetching: {res.status_code}, check api and try again')
        return res


    def get_password_leaks_count(hashes, hash_to_check):
        hashes = (line.split(':') for line in hashes.text.splitlines())
        for h, count in hashes:
            if h == hash_to_check:
                return count
        return 0


    def pwned_api_check(password):
        # Check password if it exists in API response
        sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        first5_char, tail = sha1password[:5], sha1password[5:]
        response = request_api_data(first5_char)
        print(first5_char, tail)
        return get_password_leaks_count(response, tail)


    def main(args):
        for password in args:
            count = pwned_api_check(password)
            if count:
                print(
                    f'{password} was found {count} times.. you should probably change your password')
            else:
                print(f'{password} was NOT found. Carry on!')
        return 'done!'


    if __name__ == '__main__':
        sys.exit(main(sys.argv[1:]))

```
