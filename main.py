import web_qa

class MainApp:
    def __init__(self, full_url="https://openai.com/") -> None:
        # Define root domain to crawl
        self.full_url = full_url
    
    def run(self):
        # If you have succesfully run once, you can comment out the following 3 lines ---->
        web_qa.crawl(self.full_url)
        web_qa.createScrapedCsv()
        web_qa.createEmbeddingsCsv()
         # <---- If you have succesfully run once, you can comment out the above 3 lines.

        df = web_qa.getEmbeddingsDataFrame()
        print(web_qa.answer_question(df, question="What day is it?", debug=False))
        print(web_qa.answer_question(df, question="What is our newest embeddings model?"))

if __name__ == "__main__":
    app = MainApp()
    app.run()