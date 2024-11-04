class Jar:
    """
    A class representing a cookie jar.

    Parameters
    ----------
    capacity : int, optional
        The maximum number of cookies the jar can hold (default is 12).

    Raises
    ------
    ValueError
        If the specified capacity is negative.

    Attributes
    ----------
    capacity : int
        The maximum number of cookies the jar can hold.
    size : int
        The current number of cookies in the jar.

    Methods
    -------
    __str__()
        Return a string representation of the jar with cookies represented by "🍪".
    deposit(n)
        Deposit `n` cookies into the jar.
    withdraw(n)
        Withdraw `n` cookies from the jar.

    Properties
    ----------
    jar_capacity : int
        Get the maximum number of cookies the jar can hold.
    jar_size : int
        Get the current number of cookies in the jar.

    Examples
    --------
    >>> my_jar = Jar()
    >>> my_jar.deposit(3)
    >>> my_jar.withdraw(2)
    >>> print(my_jar)
    '🍪🍪'

    """

    def __init__(self, capacity=12):
        """
        Initialize a Jar object with a specified capacity.

        Parameters
        ----------
        capacity : int, optional
            The maximum number of cookies the jar can hold (default is 12).

        Raises
        ------
        ValueError
            If the specified capacity is negative.

        """
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        """
        Return a string representation of the jar with cookies represented by "🍪".

        Returns
        -------
        str
            A string representation of the jar.

        """
        return "🍪" * self.size

    def deposit(self, n):
        """
        Deposit `n` cookies into the jar.

        Parameters
        ----------
        n : int
            The number of cookies to deposit.

        Raises
        ------
        ValueError
            If depositing `n` cookies exceeds the jar's capacity.

        """
        if (self.size + n) > self.capacity:
            raise ValueError("Exceeds jar capacity")
        self.size += n

    def withdraw(self, n):
        """
        Withdraw `n` cookies from the jar.

        Parameters
        ----------
        n : int
            The number of cookies to withdraw.

        Raises
        ------
        ValueError
            If attempting to withdraw more cookies than the jar contains.

        """
        if (self.size - n) < 0:
            raise ValueError("Withdrawal exceeds jar content")
        self.size -= n

    @property
    def jar_capacity(self) -> int:
        # Get the maximum number of cookies the jar can hold
        return self.capacity

    @property
    def jar_size(self) -> int:
        # Get the current number of cookies in the jar
        return self.size


# Example usage
my_jar = Jar()