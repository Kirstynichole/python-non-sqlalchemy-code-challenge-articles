class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        # self.author.add_article(self.magazine, self.title)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and not hasattr(self, "title") and 5 <= len(title) <= 50:
            self._title = title
        else:
            return None 

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            return None 
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            return None 

class Author:
    def __init__(self, name):
        self._name = name
        self.article_list = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name"):
            self._name = name
        else:
            # raise ValueError("Name must be a non-empty string")
            return None
    
    def add_article(self, magazine, title):
        if not hasattr(self, "_name"):
            raise ValueError("Author's name must be set before adding articles.")
        new_article = Article(self, magazine, title)
        self.article_list.append(new_article)

    def articles(self):
        # author_article_list = []
        # print(self.article_list)
        # for article in self.article_list:
        #     print(self)
        #     print(article.author)
        #     if self == article.author:
        #         author_article_list.append(article.name)
        #         print(f"author's article list: {author_article_list}")
        #         print(f"self name: {self.name}")
        # return author_article_list
        return [article.title for article in self.article_list if self == article.author]
        # return [article for article in self.article_list if self.name == article.author]

    
    def magazines(self):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            return None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and 0 < len(category):
            self._category = category
        else:
            return None

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass


author = Author("Carry Bradshaw")
magazine = Magazine("Vogue", "Fashion")
article_1 = Article(author, magazine, "How to wear a tutu with style")
article_2 = Article(author, magazine, "The art of accessorizing")

author.articles()