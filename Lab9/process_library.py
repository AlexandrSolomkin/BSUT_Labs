import xml.etree.ElementTree as ET

tree = ET.parse("library.xml")
root = tree.getroot()

print("Список книг:")
for book in root.findall("book"):
    print(f"{book.find('title').text} ({book.find('author').text}, {book.find('year').text})")

prices = [float(book.find("price").text) for book in root.findall("book")]
avg_price = sum(prices) / len(prices)
print(f"\nСредняя цена книг: {avg_price:.2f}")

genre_filter = "Фэнтези"
filtered_books = [book.find("title").text for book in root.findall("book") if book.find("genre").text == genre_filter]
print(f"\nКниги жанра {genre_filter}: {', '.join(filtered_books)}")
