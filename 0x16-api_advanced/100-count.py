#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list):
    """Prints counts of given words found in hot posts of a given subreddit.
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": "",
        "count": 0,
        "limit": 100
    }
    instances = {}
    while True:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        try:
            results = response.json()
            if response.status_code == 404:
                raise Exception
        except Exception:
            print("")
            return

        results = results.get("data")
        params["after"] = results.get("after")
        params["count"] += results.get("dist")
        for c in results.get("children"):
            title = c.get("data").get("title").lower().split()
            for word in word_list:
                if word.lower() in title:
                    times = len([t for t in title if t == word.lower()])
                    if instances.get(word) is None:
                        instances[word] = times
                    else:
                        instances[word] += times

        if params["after"] is None:
            break

    if len(instances) == 0:
        print("")
        return
    instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
    [print("{}: {}".format(k, v)) for k, v in instances]

