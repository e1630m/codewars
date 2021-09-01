class PaginationHelper:
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.ipp = items_per_page
        self.ic = len(collection)
        q, r = divmod(self.ic, self.ipp)
        self.collection = [collection[i * self.ipp:i * self.ipp + self.ipp]
            for i in range(q + (r ==0) + 1)]

    # returns the number of items within the entire collection
    def item_count(self):
        return self.ic
        
    # returns the number of pages
    def page_count(self):
        return len(self.collection)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if 0 <= page_index < self.page_count():
            return len(self.collection[page_index])
        return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or item_index >= self.item_count() or not self.item_count():
            return -1
        return item_index // self.ipp
