# 🎯 Few-Shot Prompting

**Few-shot prompting** works by providing an AI model with a **small number of examples** (or "shots") of a particular task or concept, along with instructions in the prompt.

The model then uses these examples to **generate or classify** new data that is **similar** to what it has been shown.

---

## 🧠 Why Use Few-Shot Prompting?

Few-shot prompting is especially useful in scenarios where:
- There is **limited data** available (e.g. rare languages or niche domains)
- You want to **quickly adapt models to new tasks or contexts**
- Fine-tuning is not feasible due to time or data constraints

Instead of retraining the model, you show it **a few demonstrations**, and it generalizes from them.

---

![Prompting Example](./Images/prompting_example.png)

### 🧩 One-shot vs Few-shot

- **One-shot prompting**: The model is given **one example**.
- **Few-shot prompting**: The model is given **a few examples** (typically 2–5).
- **Zero-shot prompting**: No examples are provided (see previous section).

Note: One-shot is technically a **subset** of few-shot prompting.

---

## 🧪 Demo: Zero vs One vs Few-Shot Prompting

Let’s walk through an example comparing the output of zero-shot, one-shot, and few-shot prompts.

---

### 🥶 Zero-Shot Prompt

**Prompt:**  
*Write an image description with adjectives and nouns of a Yorkshire dog running in a winter landscape in Brazil.*

**Response:**  
> A fluffy Yorkshire dog with silky, golden-brown fur dashes energetically through a serene winter landscape in Brazil. Its tiny paws kick up soft, white snow as it runs joyfully across a frost-covered meadow. Surrounding the lively pup are tall, leafless trees with delicate icicles hanging from their slender branches. A pale blue sky stretches above, casting a cool, crisp light over the sparkling snow and the dog’s glossy coat. In the distance, low hills blanketed in misty frost complete the peaceful, chilly scenery.

![Zero Shot Yorkshire Dog](./Images/zeroshotyrokshiredog.png)

> 🧩 No examples were given — the model generated a detailed description purely based on the instruction.

---

### 🧊 One-Shot Prompt

**Prompt:**  
Write a compressed, perfect image description using adjectives and nouns of a Yorkshire dog running in a winter landscape in Brazil:  
Example:  
*Blue dog, shimmering, snow, trees, frosted, ice, movements*

**Now, generate your own version:**

**Response:**  
> Exuberant Yorkshire terrier, chocolate-golden fur, frost-laden Brazilian landscape, glistening white snow, agile legs, icy crystals, sparkling eyes, twinkling frost, serene wintry scene.

![One Shot Yorkshire Dog](./Images/oneshotyorkshiredog.png)

> 🧩 The model used the structure of the provided example to compress its description effectively.

---

### 🌈 Few-Shot Prompt

**Prompt:**

Provide compressed image descriptions using adjectives and nouns of a Yorkshire dog running in a winter landscape in Brazil.

**Examples:**

1. *Blue dog, shimmering, snow, trees, frosted, ice*  
2. *Red dog, sweating, snow, flowers, frosted, ice*  
3. *Green dog, crying, snow, bees, frosted, ice*

**Now, generate your own description:**

**Response:**
> A playful blue Yorkshire dog darts through shimmering snow, surrounded by frosted trees and glistening ice.  
> A spirited red Yorkshire dog bounds energetically amid snow-covered flowers, sweating lightly while navigating the frosted ice.  
> A whimsical green Yorkshire dog races snowdrifts, tears streaming down its face, as bees buzz around the icy, frosted landscape.  
> A vivacious violet Yorkshire dog leaps gracefully across the sparkling snow, its fur fluttering like a majestic flag, while the scent of pine fills the crisp, frosty air.

![Few Shot Yorkshire Dog](./Images/fewshotyrokshiredog.png)

> 🧩 With multiple examples, the model adapted patterns and created varied, imaginative responses.

---

## 🔍 Summary

| Prompting Type | # of Examples | Control | Accuracy | Creativity |
|----------------|----------------|---------|----------|------------|
| **Zero-Shot**  | 0              | Low     | Moderate | High       |
| **One-Shot**   | 1              | Medium  | Higher   | Moderate   |
| **Few-Shot**   | 2–5            | High    | Highest  | Balanced   |

Few-shot prompting lets you **guide the model** by showing it the format, tone, and content style you want — without needing tons of data or retraining.