# books.py
from layout import serve_base_html, serve_footer
import requests
import json


def get_books_from_api():
    try:
        response = requests.get('http://localhost:5000/books')
        if response.status_code == 200:
            return response.json()
        return []
    except:
        return []


def serve_books():
    # Get books from API
    books = get_books_from_api()

    content = serve_base_html('books')
    content += """
        <div class="container mx-auto px-4 py-8">
            <h1 class="text-4xl font-bold text-center mb-8">My Book Collection</h1>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
    """

    # Generate a card for each book
    for book in books:
        # Convert book data to JSON string for the modal
        book_json = json.dumps(book).replace('"', '&quot;')

        content += f"""
                <div class="card bg-base-100 shadow-xl hover:shadow-2xl transition-shadow duration-300">
                    <figure class="px-4 pt-4">
                        <img src="{book['static_resources']['picture_url']}" alt="{book['name']}" class="rounded-xl h-64 object-cover" />
                    </figure>
                    <div class="card-body">
                        <h2 class="card-title">{book['name']}</h2>
                        <p><span class="font-semibold">Author:</span> {book['author_name']}</p>
                        <p class="text-sm mt-2 line-clamp-2">{book['description']}</p>
                        <div class="badge badge-primary mb-2">{book['category']}</div>
                        <div class="card-actions justify-end gap-2">
                            <button onclick='showBookDetails({book_json})' class="btn btn-secondary btn-sm">
                                <i class="fas fa-info-circle mr-2"></i>Details
                            </button>
                            <a href="{book['static_resources']['download_url']}" class="btn btn-primary btn-sm" target="_blank">
                                <i class="fas fa-download mr-2"></i>Download
                            </a>
                        </div>
                    </div>
                </div>
        """

    # Add modal for book details
    content += """
            </div>
        </div>

        <!-- Modal -->
        <dialog id="book_modal" class="modal">
            <div class="modal-box">
                <h3 class="font-bold text-lg" id="modal_title"></h3>
                <div class="py-4">
                    <img id="modal_image" class="w-full h-64 object-cover rounded-lg mb-4" src="" alt="">
                    <p><span class="font-bold">Author:</span> <span id="modal_author"></span></p>
                    <p><span class="font-bold">Category:</span> <span id="modal_category"></span></p>
                    <p class="mt-4"><span class="font-bold">Description:</span></p>
                    <p id="modal_description" class="mt-2"></p>
                </div>
                <div class="modal-action">
                    <a id="modal_download" href="" target="_blank" class="btn btn-primary">
                        <i class="fas fa-download mr-2"></i>Download PDF
                    </a>
                    <button class="btn" onclick="closeModal()">Close</button>
                </div>
            </div>
            <form method="dialog" class="modal-backdrop">
                <button>close</button>
            </form>
        </dialog>

        <script>
            function showBookDetails(book) {
                const modal = document.getElementById('book_modal');
                document.getElementById('modal_title').textContent = book.name;
                document.getElementById('modal_author').textContent = book.author_name;
                document.getElementById('modal_category').textContent = book.category;
                document.getElementById('modal_description').textContent = book.description;
                document.getElementById('modal_image').src = book.static_resources.picture_url;
                document.getElementById('modal_download').href = book.static_resources.download_url;
                modal.showModal();
            }

            function closeModal() {
                document.getElementById('book_modal').close();
            }
        </script>
    """

    content += serve_footer()
    return content
