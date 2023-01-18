def per(arr, p=0.5):
    """
        Returns the p-th thing from a sorted list arr 

        Parameters
        ----------
        arr : list
              the sorted list
        p   : int
              position from which to get the number in the list    
        Returns
        -------
        int
        """
    x = len(arr)
    position = int(x*p +0.5)
    return arr[max(1,min(x, position))]