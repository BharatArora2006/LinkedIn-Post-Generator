GROQ_API_KEY = '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'
from langchain_groq import ChatGroq
llm = ChatGroq(groq_api_key = GROQ_API_KEY, model_name = 'llama-3.2-11b-vision-preview')
# Checking LLM activation
if __name__ == "__main__":
  response = llm.invoke("which are top 3 pillars of a country's economy. Share in less than 50 words")
  print(response.content)

