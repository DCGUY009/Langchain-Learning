# Chain of Thought (CoT) Prompting

Large Language Models (LLMs) with over 100 billion parameters are incredibly powerful and can perform a wide range of tasks with minimal or no training. However, they still struggle with certain categories of problems — especially those requiring **multi-step reasoning**.

## Strengths and Weaknesses of LLMs

Take a quick look at what LLMs excel at, and where they tend to fall short:

✅ Summarization  
✅ Image Generation  
✅ Code Generation  
✅ Code Optimization  
❌ Multi-step Reasoning  
❌ Common Sense  
❌ Math

---

## What is Chain of Thought (CoT) Prompting?

Researchers at Google introduced **Chain of Thought (CoT) prompting**, a technique to improve LLM performance on tasks requiring reasoning. It works by breaking a complex task into a **series of intermediate steps**, helping the model to “think” through the problem logically.

---

## Standard Prompting Example

```text
Input:
Q: Shawn has five toys. For Christmas, he got two
toys each from his mom and dad. How many toys
does he have now?
A: The answer is 9.

Q: John takes care of 10 dogs. Each dog takes .5
hours a day to walk and take care of their
business. How many hours a week does he
spend taking care of dogs?
A:
```

**Model Output:**
```
The answer is 50.
```

> In this case, the model answers incorrectly due to lack of reasoning steps.

---

## Chain of Thought (CoT) Prompting Example

```text
Input:
Q: Shawn has five toys. For Christmas, he got two
toys each from his mom and dad. How many toys
does he have now?
A: Shawn started with 5 toys. If he got 2 toys each
from his mom and dad, then that is 4 more toys. 5
+ 4 = 9, The answer is 9.

Q: John takes care of 10 dogs. Each dog takes
.5 hours a day to walk and take care of their
business. How many hours a week does he
spend taking care of dogs?
John takes care of IO dogs. Each dog takes .5
```

**Model Output:**
```
hours a day to walk and take care of their
business. So that is 10 x .5 = 5 hours a day. 5
hours a day x 7 days a week = 35 hours a week,
The answer is 35 hours a week.
```

> The model performs better by reasoning through each step before arriving at the answer.

---

## Zero-Shot CoT Prompting

To invoke reasoning without examples, simply **prefix the prompt** with:

```
"Let's think step by step."
```

This instructs the model to format its output with reasoning steps.

---

## Few-Shot CoT Prompting

Provide a few examples of `<question, answer>` pairs, where each **answer includes step-by-step reasoning**. This helps the model learn the format and replicate the reasoning process in its response.

Sure! Here's a clean example of **Few-Shot Chain of Thought (CoT) Prompting**, formatted for clarity:

> Let's see an example of Few-Shot CoT Prompting where each answer is explained step-by-step. This teaches the model to reason similarly for new inputs.

---

### Prompt:
```
Q1: Sarah has 3 boxes of pencils. Each box has 12 pencils. She gave 10 pencils to her friend. How many pencils does she have now?
A1: Sarah has 3 boxes with 12 pencils each. That’s 3 × 12 = 36 pencils. She gave away 10, so 36 − 10 = 26. The answer is 26.

Q2: Tom read 15 pages on Monday, 20 on Tuesday, and 25 on Wednesday. How many pages did he read in total?
A2: Tom read 15 + 20 + 25 pages. That’s 60 pages in total. The answer is 60.

Q3: A factory makes 120 cars per day. How many cars does it make in a week?
A3: A week has 7 days. So, 120 × 7 = 840. The answer is 840.

Q4: Lisa has 5 packs of stickers. Each pack contains 18 stickers. She gives away 24 stickers. How many does she have left?
A4:
```

---

### 💡 Model Output:
```
Lisa has 5 packs with 18 stickers each. That’s 5 × 18 = 90 stickers. She gives away 24, so 90 − 24 = 66. The answer is 66.
```

---

This is Few-Shot CoT in action: giving 3–5 similar examples helps the model mimic step-by-step reasoning in its response.
---