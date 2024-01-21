import web_qa

class MainApp:
    def __init__(self, domain="openai.com", full_url="https://openai.com/") -> None:
        # Define root domain to crawl
        web_qa.domain = domain
        web_qa.full_url = full_url
    
    def run(self):
        # web_qa.crawl()
        # web_qa.createScrapedCsv()
        # web_qa.createEmbeddingsCsv()
        df = web_qa.getEmbeddingsDataFrame()
        print(web_qa.answer_question(df, question="What day is it?", debug=False))
        print(web_qa.answer_question(df, question="What is our newest embeddings model?"))

if __name__ == "__main__":
    app = MainApp()
    app.run()