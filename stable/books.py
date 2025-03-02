# books.py
from layout import serve_base_html, serve_footer


def serve_books():
    # Sample book data - in a real implementation, this might come from a database
    books = [
        {
            "name": "The Clean Coder",
            "category": "Software Development",
            "author": "Robert C. Martin",
            "image": "https://m.media-amazon.com/images/I/51sZW87slRL._SY445_SX342_.jpg"
        },
        {
            "name": "Atomic Habits",
            "category": "Self-Help",
            "author": "James Clear",
            "image": "https://m.media-amazon.com/images/I/51-nXsSRfZL._SY445_SX342_.jpg"
        },
        {
            "name": "The Pragmatic Programmer",
            "category": "Software Development",
            "author": "Andrew Hunt & David Thomas",
            "image": "https://m.media-amazon.com/images/I/51cUVaBWZzL._SY445_SX342_.jpg"
        },
        {
            "name": "Thinking, Fast and Slow",
            "category": "Psychology",
            "author": "Daniel Kahneman",
            "image": "https://m.media-amazon.com/images/I/41wI53OEpCL._SY445_SX342_.jpg"
        }
    ]

    content = serve_base_html('books')
    content += """
        <div class="container mx-auto px-4 py-8">
            <h1 class="text-4xl font-bold text-center mb-8">My Book Collection</h1>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
    """

    # Generate a card for each book
    for book in books:
        content += f"""
                <div class="card bg-base-100 shadow-xl hover:shadow-2xl transition-shadow duration-300">
                    <figure class="px-4 pt-4">
                        <img src="{book['image']}" alt="{book['name']}" class="rounded-xl h-64 object-cover" />
                    </figure>
                    <div class="card-body">
                        <h2 class="card-title">{book['name']}</h2>
                        <p><span class="font-semibold">Author:</span> {book['author']}</p>
                        <div class="badge badge-primary">{book['category']}</div>
                    </div>
                </div>
        """

    content += """
            </div>
        </div>
    """

    content += serve_footer()
    return content
