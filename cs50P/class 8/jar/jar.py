class Jar:
    def __init__(self, capacity=12):
        if int(capacity) < 0:
            raise ValueError("negative number")
        else:
            self._capacity = capacity
            self._size = 0

    def __str__(self):
        self.cookies = self._size * "🍪"
        return self.cookies

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError
        else:
            self._size = self._size + n

    def withdraw(self, n):
         if self._size - n < 0:
            raise ValueError
         else:
            self._size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    numnum = Jar("10")
    print(numnum)


main()
