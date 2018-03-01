class Book:
  def __init__(self, title, pub, author="L. Ron Hubbard"):
    self.title = title
    self.pub = pub
    self.author = author

battlefield = Book("Battlefield Earth",
                   "St. Martin's Press")
martian = Book(title="The Martian Chronicles", 
               author="Ray Bradbury", 
               pub="Doubleday")
