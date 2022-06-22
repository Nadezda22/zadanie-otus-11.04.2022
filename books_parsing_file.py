def divide_books_between_users(books, users):
    count_books = len(books) // len(users)
    max_users = len(books) % len(users)
    prev_index = 0
    tmp = []
    for i in range(0, len(users)):
        next_index = prev_index + count_books
        if i in range(max_users):
            next_index = prev_index + count_books + 1
        tmp.append(books[prev_index:next_index])
        prev_index = next_index
    return tmp
