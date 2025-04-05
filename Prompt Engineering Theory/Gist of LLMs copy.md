What is a Language Model?
It is a distribution of probabilities over a sequence of words (Definition from wikipedia)

So, it's about predicting the next word correctly based on the probability of that next word occurring.
Let's take an example:
We have a sentence like "Langchain is a ___________"
Now, the possible options for that blank could be
1. Framework
2. Library 
3. Banana
4. Fruit 

Now, probabilities for each of this word is calculated and they are placed in the blank. So, let's say the probabilities for the words are:
1. Framework: 0.99
2. Library: 0.8
3. Banana: 0.1
4. Fruit: 0.1

So, the highest probability of the next word would be "Framework". That is how a Language Model works.

So, to understand simply in a mathematical notation:
![Language Model](./Images/language_model.png)

Here x(t+1) has to be a word in our vocabulary V

So, to summarize language model, it is simply the idea that we have a sentence and we are going to predict the next word that might occur based on the probability. This is super super similar to autocomplete in Gmail, Text Messages or in Google Search. These are language models working to give you the next probable word.

Similar to this, a large language model is a language model which is trained on a large amount of data and it is really good at calculating the probabilties and deriving at the next most probable word.

And sometimes that is why hallucinations in LLM occur since they are just calculating the probabilites and giving the next word.
