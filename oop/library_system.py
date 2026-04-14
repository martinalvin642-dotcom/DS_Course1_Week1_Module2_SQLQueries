# ============================================================
#  Library Management System
# ============================================================

class LibraryItem:
    """
    Base class for all library items.
    Tracks checkout history and enforces availability logic.
    """

    _total_items = 0  # class-level counter shared across all instances

    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True
        self.checkout_history = []        # list of dicts: {action, librarian}
        LibraryItem._total_items += 1

    # ── core methods ──────────────────────────────────────────

    def display_info(self):
        status = "Available" if self.is_available else "Checked Out"
        print(f"  Title            : {self.title}")
        print(f"  Author           : {self.author}")
        print(f"  Publication Year : {self.publication_year}")
        print(f"  Status           : {status}")

    def checkout(self, patron="Unknown"):
        if not self.is_available:
            print(f"  Sorry! '{self.title}' is already checke--d out.")
            return False
        self.is_available = False
        self.checkout_history.append({"action": "checked out", "patron": patron})
        print(f"  '{self.title}' checked out to {patron}.")
        return True

    def return_item(self, patron="Unknown"):
        if self.is_available:
            print(f"  '{self.title}' is already in the library.")
            return False
        self.is_available = True
        self.checkout_history.append({"action": "returned", "patron": patron})
        print(f"  '{self.title}' returned by {patron}. Thank you!")
        return True

    # ── extras ────────────────────────────────────────────────

    def show_history(self):
        """Print the full checkout/return history for this item."""
        if not self.checkout_history:
            print(f"  No history for '{self.title}'.")
            return
        print(f"  History for '{self.title}':")
        for i, entry in enumerate(self.checkout_history, 1):
            print(f"    {i}. {entry['action'].capitalize()} by {entry['patron']}")

    @classmethod
    def total_items(cls):
        """Return how many LibraryItem instances have been created."""
        return cls._total_items

    def __repr__(self):
        status = "available" if self.is_available else "checked out"
        return f"<{self.__class__.__name__}: '{self.title}' ({self.publication_year}) — {status}>"

    def __str__(self):
        return f"{self.__class__.__name__}: {self.title} by {self.author}"


# ── Book ──────────────────────────────────────────────────────

class Book(LibraryItem):
    """A physical book with ISBN and publisher info."""

    def __init__(self, title, author, publication_year, isbn, publisher):
        super().__init__(title, author, publication_year)
        self.isbn = isbn
        self.publisher = publisher

    def display_info(self):
        print(f"\n{'='*40}")
        print(f"  BOOK")
        print(f"{'='*40}")
        super().display_info()
        print(f"  ISBN             : {self.isbn}")
        print(f"  Publisher        : {self.publisher}")
        print(f"{'='*40}\n")

    @classmethod
    def from_isbn(cls, isbn, title, author, year, publisher):
        """Factory method — create a Book directly from its ISBN."""
        return cls(title, author, year, isbn, publisher)


# ── Magazine ──────────────────────────────────────────────────

class Magazine(LibraryItem):
    """A periodical with issue and month metadata."""

    MONTHS = [
        "", "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    def __init__(self, title, author, publication_year, issue_number, publication_month):
        super().__init__(title, author, publication_year)
        self.issue_number = issue_number
        self.publication_month = publication_month

    @property
    def month_name(self):
        """Returns the full month name instead of a bare number."""
        if 1 <= self.publication_month <= 12:
            return self.MONTHS[self.publication_month]
        return "Unknown"

    def display_info(self):
        print(f"\n{'='*40}")
        print(f"  MAGAZINE")
        print(f"{'='*40}")
        super().display_info()
        print(f"  Issue Number     : #{self.issue_number}")
        print(f"  Published        : {self.month_name} {self.publication_year}")
        print(f"{'='*40}\n")


# ── DVD ───────────────────────────────────────────────────────

class DVD(LibraryItem):
    """A DVD with duration, director, and a dynamic genre set."""

    def __init__(self, title, publication_year, duration, director, genres, author="N/A"):
        super().__init__(title, author, publication_year)
        self.duration = duration
        self.director = director
        self.genres = set(genres)  # defensive copy — always a set

    @property
    def runtime(self):
        """Returns duration as a human-readable string."""
        hours, mins = divmod(self.duration, 60)
        return f"{hours}h {mins}m" if hours else f"{mins}m"

    def add_genre(self, genre):
        genre = genre.strip().title()   # normalise capitalisation
        if genre in self.genres:
            print(f"  '{genre}' is already listed as a genre.")
        else:
            self.genres.add(genre)
            print(f"  Genre '{genre}' added to '{self.title}'.")

    def remove_genre(self, genre):
        genre = genre.strip().title()
        self.genres.discard(genre)
        print(f"  Genre '{genre}' removed from '{self.title}'.")

    def display_info(self):
        print(f"\n{'='*40}")
        print(f"  DVD")
        print(f"{'='*40}")
        super().display_info()
        print(f"  Director         : {self.director}")
        print(f"  Runtime          : {self.runtime}")
        print(f"  Genres           : {', '.join(sorted(self.genres))}")
        print(f"{'='*40}\n")


# ── LibrarySystem ─────────────────────────────────────────────

class LibrarySystem:
    """
    Optional manager class — stores all items and supports
    searching, listing, and availability reports.
    """

    def __init__(self, name):
        self.name = name
        self._catalog = []

    def add_item(self, item):
        self._catalog.append(item)
        print(f"  Added: {item}")

    def search(self, query):
        """Case-insensitive search across title, author, and director."""
        q = query.lower()
        results = [
            item for item in self._catalog
            if q in item.title.lower()
            or q in item.author.lower()
            or (hasattr(item, "director") and q in item.director.lower())
        ]
        return results

    def available_items(self):
        return [item for item in self._catalog if item.is_available]

    def report(self):
        total = len(self._catalog)
        available = len(self.available_items())
        print(f"\n  {self.name} — Catalog Report")
        print(f"  Total items   : {total}")
        print(f"  Available     : {available}")
        print(f"  Checked out   : {total - available}")
        print()


# ============================================================
#  Tests
# ============================================================

print("\n--- Creating items ---\n")

book = Book(
    title="The Pragmatic Programmer",
    author="Andrew Hunt & David Thomas",
    publication_year=1999,
    isbn="978-0201616224",
    publisher="Addison-Wesley"
)

book2 = Book.from_isbn(              # factory classmethod
    isbn="978-0132350884",
    title="Clean Code",
    author="Robert C. Martin",
    year=2008,
    publisher="Prentice Hall"
)

magazine = Magazine(
    title="National Geographic",
    author="Various Authors",
    publication_year=2024,
    issue_number=6,
    publication_month=6
)

dvd = DVD(
    title="Inception",
    publication_year=2010,
    duration=148,
    director="Christopher Nolan",
    genres={"Sci-Fi", "Thriller"}
)

print("\n--- Display info ---")
book.display_info()
magazine.display_info()
dvd.display_info()

print("\n--- Checkout & return ---\n")
book.checkout(patron="Alice Kariuki")
book.checkout(patron="Bob Mwangi")   # already checked out — should warn
book.return_item(patron="Alice Kariuki")
book.show_history()

print("\n--- DVD genre management ---\n")
dvd.add_genre("action")              # auto-capitalised to "Action"
dvd.add_genre("Sci-Fi")             # duplicate — should warn
dvd.remove_genre("Thriller")
dvd.display_info()

print("\n--- LibrarySystem ---\n")
library = LibrarySystem("Nairobi City Library")
for item in [book, book2, magazine, dvd]:
    library.add_item(item)

library.report()

results = library.search("nolan")
print(f"  Search 'nolan': {results}\n")

print(f"\n  Total LibraryItem instances ever created: {LibraryItem.total_items()}")
print(f"\n  repr demo: {repr(dvd)}")
print(f"  str  demo: {str(book)}\n")