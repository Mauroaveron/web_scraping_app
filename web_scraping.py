import bs4
import requests

# Extract from the site catalog the titles of the books whose rating is 4 or 5 stars.

# Create an url without page number
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

# List of titles with 4 or 5 stars
high_rating_titles = []

# Iterate pages
for page in range(1, 51):

    # Create soup in each page
    page_url = base_url.format(page)
    result = requests.get(page_url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')

    # Select data from books
    books = soup.select('.product_pod')

    # Iterate books
    for book in books:

        # Check if they have 4 or 5 stars
        if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) != 0:

            # Save title in variable
            book_title = book.select('a')[1]['title']

            # Add book title to the list
            high_rating_titles.append(book_title)

# Print 4 or 5 stars books in console
for t in high_rating_titles:
    print(t)
