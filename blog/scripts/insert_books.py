import blog.models as models
import csv
import os

def insert_books():
    workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
    path = os.path.join(workpath,'books.csv')
    print('yay')
    with open(path, 'r', encoding='utf-8') as f:
    # ignore the first row, as it is the header row.
        next(f, None)
        reader = csv.reader(f, escapechar='\\', delimiter=',')
        for row in reader:
            book=models.books(
                bookID =int(row[0]),
                title = str(row[1]),
                authors =row[2] ,
                average_rating =float(row[3]) ,
                isbn = row[4],
                isbn13 = row[5],
                language_code =row[6] ,
                num_pages = int(row[7]),
                ratings_count = int(row[8]),
                text_reviews_count =int(row[9]),
                publication_date = row[10],
                publisher = row[11],
            )
            book.save()
