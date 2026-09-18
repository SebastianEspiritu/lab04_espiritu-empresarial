from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name


class AuthorProfile(models.Model):
    # OneToOneField: Separates biographical details from primary author record
    author = models.OneToOneField(
        Author, 
        on_delete=models.CASCADE, 
        related_name='profile'
    )
    biography = models.TextField()
    website = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Author Profile"
        verbose_name_plural = "Author Profiles"

    def __str__(self):
        return f"Profile of {self.author.name}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    
    # ForeignKey: One author can write many books
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books'
    )
    
    # ManyToManyField simple: A book can have multiple categories
    categories = models.ManyToManyField(
        Category, 
        related_name='books'
    )
    
    # ManyToManyField with custom intermediate table (through)
    publishers = models.ManyToManyField(
        Publisher, 
        through='Publication', 
        related_name='books'
    )

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title


class Publication(models.Model):
    # Intermediate model saving publication date and edition number
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    edition = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"
        unique_together = ('book', 'publisher', 'edition')

    def __str__(self):
        return f"{self.book.title} - {self.publisher.name} (Ed. {self.edition})"