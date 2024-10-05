# Semantic Similarity
## Introduction
* The system approximates the semantic similarity of any pair of words. The **semantic similarity** between two words is the measure of the closeness of their meanings.
   * For example, the semantic similarity between “car” and “vehicle” is high, while that between “car” and “flower” is low.
* Given a word $w$ and a list of potential synonyms $s1, s2, s3, s4$, we compute the similarities of $(w, s1), (w, s2), (w, s3), (w, s4)$ and choose the word whose similarity to w is the highest.
* We will measure the semantic similarity of pairs of words by first computing a **semantic descriptor vector** of each of the words, and then taking the similarity measure to be the **cosine similarity** between the two vectors.
## Cosine Similarity
$$sim(u,v)=\frac{u\cdot v}{|u||v|}=\frac{\sum_{i=1}^N u_iv_i}{\sqrt{(\sum_{i=1}^N u_i^2)(\sum_{i=1}^N v_i^2)}}$$
