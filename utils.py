import os

from langchain.chains import LLMChain
from langchain_community.llms import GPT4All, LlamaCpp

import os 
import dotenv
dotenv.load_dotenv()

model_path = os.getenv('model_path')


class BaseStructureChain:

    PROMPT = ''

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
