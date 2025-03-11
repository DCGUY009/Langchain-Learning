## LangChain Documentation Helper

For Documentation Scraping of Langchain version v1, I have used this command (In git bash as powershell is considering wget as -Web Invoke and not considering some options of wget):
```bash
wget -r -A.html -P langchain-docs https://api.python.langchain.com/en/v0.1/langchain_api_reference.html
```

For Documentation Scraping of Langchain version v1, I have used this command (In git bash as powershell is considering wget as -Web Invoke and not considering some options of wget):
```bash
wget -r -A.html -P langchain-docs https://api.python.langchain.com/en/v0.0.354/langchain_api_reference.html
```

Just keep in mind that the link will get outdated or changed and this may not work at a later time, simply follow the link and find out the new one.


Add this note at 1:15 in Section 6 and Pinecone Vectorstore Ingestion video:
There is a ReadtheDocs that is used to create the documentation for many opensource github repositories. (Example: https://api.python.langchain.com/en/v0.0.354/langchain_api_reference.html). Even langchain documentation is written this way. So, ReadtheDocsLoader in langchain is used for such types of documentations which we just scraped using the wget command:

wget -r -A.html -P langchain-docs https://api.python.langchain.com/en/v0.0.354/langchain_api_reference.html 