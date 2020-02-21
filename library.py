class Library:
    def __init__(self, lib_id, bc, ts, bs, books, book_score):
        self.lib_id = lib_id
        self.books_count = bc
        self.time_to_signup = ts
        self.ship_per_day = bs
        self.books = books
        self.scanned_books = []
        self.book_score = book_score
        self.score = bs / ts

    def library_book_score(self):
        accumulator = 0
        for i in self.books:
            accumulator += self.book_score[i]
        return accumulator

    def check_sim(self, other):
        self_set = set(self.books)

        acc = 0
        for i in other.books:
            if i in self_set:
                acc += 1
        return acc

    def __lt__(self, other):
        return self.score > other.score

    def __str__(self):
        new_str = "Lib_ID: " + str(self.lib_id) + \
                  "\n" + \
                  "Book count: " + str(self.books_count) + \
                  "\n" + \
                  "Time_to_signup: " + str(self.time_to_signup) + \
                  "\n" + \
                  "Ship per day: " + str(self.ship_per_day) + \
                  "\n" + \
                  "Book list: " + str(self.books)
        return new_str
