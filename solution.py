from library import *

filename = 'd_tough_choices.txt'
f = open('files/' + filename, 'r')

BOOKS, LIBS, DAYS = map(int, f.readline().split())
temp_libs = LIBS

books_score = list(map(int, f.readline().split()))

libraries = []
libraries.sort()

while LIBS > 0:
    lib_info = list(map(int, f.readline().split()))

    lib_books = list(map(int, f.readline().split()))
    lib = Library(temp_libs - LIBS, lib_info[0], lib_info[1], lib_info[2], lib_books)
    libraries.append(lib)

    LIBS -= 1


def sort_by_book_score(lib):
    res = []

    for i in (lib.books):
        tuple = (books_score[i], i)
        res.append(tuple)

    res.sort(reverse=True)

    result_arr = []

    for j in res:
        result_arr.append(j[1])

    return result_arr


# print(libraries[0])
# print(libraries[1])

scanned_libs = []
scanned_books = set()

while DAYS > 0:
    # print(DAYS)
    current_lib = libraries.pop()
    DAYS -= current_lib.time_to_signup
    scanned_libs.append(current_lib)

    book_order = sort_by_book_score(current_lib)
    current_index = 0
    days_left = DAYS
    num_signs_per_day = current_lib.ship_per_day
    for i in range(days_left):
        j = num_signs_per_day
        while j > 0:
            if book_order[current_index] not in scanned_books:
                scanned_books.add(book_order[current_index])
                current_lib.scanned_books.append(book_order[current_index])
                j -= 1
            if current_index >= len(book_order) - 1:
                break
            current_index += 1

        if current_index >= len(book_order):
            break
    if len(libraries) == 0:
        break

# print(scanned_libs[0].scanned_books)
# print(scanned_libs[1].scanned_books)

output = open(filename + 'output', 'a')

output.write(str(len(scanned_libs)) + '\n')
ii=0
for each in scanned_libs:
    if len(each.scanned_books) == 0:
        ii += 1
        continue
    output.write(str(each.lib_id) + ' ' + str(len(each.scanned_books)) + '\n')
    output.write(' '.join(list(map(str, each.scanned_books))) + '\n')
print(ii)

