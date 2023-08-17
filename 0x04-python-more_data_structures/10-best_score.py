#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Retrieves the key associated with the highest integer value in the dict
    Returns
    -------
    str or None
        Returns the key with the highest integer value. 
        If no valid score is found, returns None.
    """
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    max_key = max(a_dictionary, key=a_dictionary.get)
    return max_key
