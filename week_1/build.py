import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
class ChatBot:
    def __init__(self,model,base_url):
        self.messages = []
        self.model = model
        self.base_url = base_url
        self.tokens = 0
        self.client = OpenAI(
            base_url = self.base_url,
            api_key = os.environ["OPENROUTER_API_KEY"],
        )
    
    def call_model(self,prompt: str) -> str:
        self.messages.append({"role": "user", "content": prompt})
        response = self.client.chat.completions.create(
        model=self.model,
        messages = self.messages,
    )
        self.tokens += response.usage.total_tokens
        return response.choices[0].message.content
    
    def summary(self,l):
        p = ""
        for i in l:
            p = p + i["content"]
        prompt = "following two are either question, response or a summary, summarize it in less characters as possible without losing key information,write it so that it can be given to system of another ai agent:"+","+p
        output = self.call_model(prompt)
        return [{"role":"system","content":output}]

    
    def run_model(self):
        print("Chat with AI Agent started , Type Exit to stop,Type Summary for a summary of the chat")
        while True:
            if len(self.messages) > 25:
                self.messages =self.summary(self.messages)
            prompt = input("[YOU]: ")
            if prompt.lower() == "exit":
                break
            if prompt.lower() == "summary":
                print(self.summary(self.messages)[0]["content"])
                print(self.tokens)
                print()
                continue
            output = self.call_model(prompt)
            print("[AGENT]: "+output)
            print(f"Tokens used:{self.tokens}")
            print()
            self.messages.append({"role":"assistant","content":output})

henry = ChatBot(model = input("Enter Model name: "),base_url = "https://openrouter.ai/api/v1")
henry.run_model()
