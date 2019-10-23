class TwoSum:

    def __init__(self):
        self.container = {}

    """
    @param number: An integer
    @return: nothing
    """

    def add(self, number):
        # write your code here
        self.container[number] = self.container.get(number, 0) + 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        for number, count in self.container.items():
            if value - number == number:
                if count > 1:
                    return True
            elif value - number in self.container:
                return True

        return False