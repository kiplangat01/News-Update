class Source:
    def __init__(self,id,name, description,language,country,category,url):
        self.name=name
        self.id=id
        self.category=category
        self.description=description
        self.language=language
        self.country=country
        self.url=url



class Article:
    def __init__(self,source, title, author,descrpition, urlimage,publishedAt,content,url):
        self.source=source
        self.title=title
        self.author=author
        self.description=descrpition