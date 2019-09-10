class Article:
    """
    Article class defines Article objects
    """

    def __init__(self,author,title,description,article_url,image_url,date_created):
        self.author = author
        self.title = title
        self.description = description
        self.article_url = article_url
        self.image_url = image_url
        self.date_created = date_created    

class Sources:
    """
    Sources class defines the source objects of our news
    """
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country