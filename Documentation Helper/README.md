## LangChain Documentation Helper

For Documentation Scraping of Langchain version v1, I have used this command in git bash (as powershell is considering wget as -Web Invoke and not considering some options of wget):
```bash
wget -r -A.html -P langchain-docs https://api.python.langchain.com/en/v0.1/langchain_api_reference.html
```

For Documentation Scraping of Langchain version v3, I have used this command in git bash (as powershell is considering wget as -Web Invoke and not considering some options of wget):
```bash
wget -r -A.html -P langchain-docs https://api.python.langchain.com/en/v0.0.354/langchain_api_reference.html
```

Just keep in mind that the link will get outdated or changed and this may not work at a later time, simply follow the link and find out the new one.

This is just a sample implementation of the help we can get using langchain documentation. Langchain itself has built a chatbot which can help you with anything regarding langchain documentation. It is production level RAG and it is open source:

Chatbot Link: [Langchain Documentation Helper by Langchain Chatbot](https://chat.langchain.com/)

Github Link: [Langchain Documentation Helper by Langchain Open Source Github Code](https://github.com/langchain-ai/chat-langchain)
