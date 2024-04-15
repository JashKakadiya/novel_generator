import os
from langchain.document_loaders import PyPDFLoader
from langchain.llms import GPT4All, LlamaCpp
import dotenv
dotenv.load_dotenv()
model_path = os.getenv('model_path')
from langchain.chains import LLMChain

class MainCharacterChain:

    PROMPT = """
    You are provided with the resume of a person. 
    Describe the person's profile in a few sentences and include that person's name.

    Resume: {text}

    Profile:"""

    def __init__(self) -> None:

        self.llm = LlamaCpp(
    model_path=model_path,
    max_tokens=1024,
    n_gpu_layers=40,
    n_batch=512,
    verbose=True,
    n_ctx=4096, # Context window

    temperature = 0.75,
)
        self.chain = LLMChain.from_string(
            llm=self.llm,
            template=self.PROMPT
        )

        self.chain.verbose = True

    def load_resume(self, file_name):

        file_path = os.path.join(os.path.dirname(__file__),'docs', file_name)
        loader = PyPDFLoader(file_path)
        docs = loader.load_and_split()
        return docs

    def runs(self, file_name):
        docs = self.load_resume(file_name)
        resume = '\n\n'.join([doc.page_content for doc in docs])
        # print(resume)
        return self.chain.run(resume)
