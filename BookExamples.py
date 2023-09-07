class Book():
    def binarySearch(self, item, listN):
        high = len(listN)-1
        low = 0
        while high >= low:
            mid = (high+low)/2
            mid = int(mid)
            if listN[mid] == item:
                return mid
            if listN[mid] > item:
                high = mid-1
            elif listN[mid] < item:
                low = mid +1
        return None

b = Book()
print(b.binarySearch(2,[1,2,3,4,5]))
print(b.binarySearch(4,[1,2,3,4,5]))
print(b.binarySearch(8,[1,2,3,4,5,6]))
print(b.binarySearch(2,[1,2,3,4,5,6]))
print(b.binarySearch(4,[1,2,3,4,5,6]))

