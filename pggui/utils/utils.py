def clamp(value, mini=None, maxi=None):
    """
        Block value between mini and maxi

        Parameters
        ----------
        value: 
            Actual value
        mini: 
            Minimum value
        maxi: 
            Maximum value

        Returns
        -------
        Final value
    """
    if mini is not None and value < mini:
        return mini
    elif maxi is not None and value > maxi:
        return maxi
    return value