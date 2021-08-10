class Sources:
    '''
    Sources class to define Sources Objects
    '''

    def __init__(self, id, name, description, url, category, country, language):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language

class Articles:
    '''
    Articles class to define Articles object 
    '''
    def __init__(self, title,descripion, url, urlToImage, publishedAt):
        self.title = title 
        self.descripion = descripion
        self.url =url 
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
