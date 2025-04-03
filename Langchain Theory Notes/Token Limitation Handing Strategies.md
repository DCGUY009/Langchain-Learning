Every LLM have a token limit. Now, gpt-4o-mini has a context length of 128k tokens and gemini has 1M tokens, etc. This keeps on increasing as GPU's becomes cheaper and models become better. 

Now what is this context length. LLMs operate in terms of tokens. A token can be a set of letters in a word or a whole word or a bunch of words, it is determined by the vendor of the llm based on the model needs at the time of the training. So, they use a tokenizer which divides this words into tokens based on the model needs. Now, it can be different for each model. So, let's say we have 3 models:

1. Claude 3.5 is a model optimized for coding purposes. So, here the tokenizer would make sure not to divide the meaningful units like def, () or {} so that the llm doesn't loose important context

2. Gpt models use BPE. which balances efficiency across various text types. including conversational language, prose, and code

3. Google Gemini might have a tokenizer optimized for multi lingual text

So, this context limit of 128k (let's assume gpt 4o mini) is combined of input and output. Now, if input and output combined exceeds this limit, then llm might not give accurate answer (as now it is cutting off and taking only the words that fall under that context limit directly rather than throwing an error).So, there are some methods in langchain to deal with this. Let's see them here.

They are:

1. Stuffing

2. Map reduce

3. Refine, etc


So, this code

langchain.chains.summarize import load_summarize_chain
docs = [Document(page_content=t) for t in texts[:3]]
chain = load_summarize_chain(llm, chain_type="stuff")
chain.run(docs)
So, lets say we have a bunch of documents we want to summarize. We can use thos load_summarize_chain from langchain and it will use this chain and summarize the documents provided.



Now, here in the above code when we intialized this chain, we are using this something called as chain_type = "stuff". This simply means that whatever we are passing in as context is being directly put in the prompt (stuffed). This will work fine for one llm call and it will fail when there are large documents, or memory is integrated or multiple llm calls happen (like in agents)

So, to mitigate this what we can do is use something called as map_reduce. Here, what happens is each document is summarized with the help of an llm (this can happen asynchronously since there is no dependency of one document over the another) and then these all small summaries from individual documents are combined to make a big summary (which is the final summary of the document).

The code in langchain is simple in the earlier load_summarize_chain we use chain_type="map_reduce"

The advantages and disadvantages of using map_reduce is that:
Advantages: Can scale to any number of documents and also can run in parallel
Disadvantages: Cost will increase and also possible loss of information 

The next way to handle this using refine chain: 




