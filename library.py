class Library:
    def __init__(self, lib_id, bc, ts, bs, books):
        self.lib_id = lib_id
        self.books_count = bc
        self.time_to_signup = ts
        self.ship_per_day = bs
        self.books = books
        self.scanned_books = []


    def __lt__(self, other):
        return self.time_to_signup < other.time_to_signup

    def __str__(self):
        new_str = "Lib_ID: " + str(self.lib_id) + \
                  "\n" +\
                  "Book count: " + str(self.books_count) + \
                  "\n" + \
                  "Time_to_signup: " + str(self.time_to_signup) + \
                  "\n" + \
                  "Ship per day: "+str(self.ship_per_day) + \
                  "\n" + \
                  "Book list: " + str(self.books)
        return new_str


