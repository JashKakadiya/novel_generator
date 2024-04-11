import os

from langchain.chains import LLMChain
# from langchain.chat_models import ChatOpenAI
from langchain.llms import GPT4All, LlamaCpp

import os 
# Add api key here:
import dotenv
dotenv.load_dotenv()

model_path = os.getenv('model_path')


class BaseStructureChain:

    PROMPT = ''

    def __init__(self) -> None:
        self.llm = LlamaCpp(model_path=model_path, n_ctx=4096, verbose=False)
        self.chain = LLMChain.from_string(
            llm=self.llm,
            template=self.PROMPT,
        )
        self.chain.verbose = True

class BaseEventChain:
    
    PROMPT = ''

    def __init__(self) -> None:

        self.llm = LlamaCpp(model_path=model_path, n_ctx=4096, verbose=False)
        self.chain = LLMChain.from_string(
            llm=self.llm,
            template=self.PROMPT,
        )

        self.chain.verbose = True
