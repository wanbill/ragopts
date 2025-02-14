# ragopts

# Table to Text: Graph Augmented Table Retrieval :bar_chart:

**Group 9**  
**Authors:** How-Yeh Wan, Xukun Liu, Jingyu Wu  
**Date:** 02 June, 2024

---

## Agenda Overview :clipboard:
1. **Scenario**
2. **Motivation**
3. **Solution**
4. **Methodology**
5. **Dataset**
6. **Result Analysis**
7. **Future Works**
8. **Q & A**

---

## Existing Works :books:
- **Approach 1:** Use language models to generate summaries based on selected rows or columns.
- **Approach 2:** Use Retrieval Augmented Generation (RAG) with LLMs to generate responses.  
  _Note:_ RAG provides clear intermediate steps and reduces hallucinations.

---

## Motivation :warning:
- **Dependency Issues:** The RAG framework struggles to handle dependencies when answers depend on multiple values.
- **Cost Concerns:** Multiple retrieval queries increase token costs, latency, and context length, potentially impacting model performance.

---

## Proposed Solution :sparkles:
- **Enhancing Dependency Handling:** Integrate knowledge graphs to return query values along with associated information.
- **Reducing Retrieval Overhead:** Use the inherent relevance of query values to minimize the number of necessary retrievals.

---

## Methodology :gear:
- **AgentMain:** Manages user interaction and communicates with the ChatGPT-4 API.
- **AgentEdge:** Responsible for establishing edges between nodes by identifying their enumeration types (utilizing ChatGPT-3.5).
- **Design Choice:** A flexible node structure that accommodates detailed information storage and efficient graph traversal.

---

## Dataset Description :bar_chart:
- **Data Source:** Financial reports from Yahoo Finance using the yfinance API.
- **Example Dataset:** Balance sheet of Apple Inc.
- **Process:** Web scraping financial reports to extract tables, whose dependencies serve as the ground truth for evaluation.

---

## Experiments & Results :chart_with_upwards_trend:
- **Semantic Edge Construction:** Evaluated by comparing the number of correctly built edges.
- **Real-world Performance:**  
  - With Graph: **Accuracy = 100%**  
  - Without Graph: **Accuracy = 62.5%**
- **Example Queries:**  
  - Calculate percentage changes in total assets.
  - Determine values for cash equivalents and inventory.
  - Sum multiple financial metrics.

---

## Limitations & Future Works :seedling:
- **Current Limitation:** The embedding function shows low robustness to minor variations in input text.
- **Future Direction:** Improve the embedding function to enhance tolerance to textual variations and overall performance.

---

## Sources & References :link:
- [Why you shouldn't invest in vector databases](https://blog.det.life/why-you-shouldnt-invest-in-vector-databases-c0cd3f59d23c)
- [Try Chroma](https://www.trychroma.com/)
- [Chromaviz on GitHub](https://github.com/mtybadger/chromaviz?tab=readme-ov-file)
- [Stardog Knowledge Graph](https://www.stardog.com/knowledge-graph/)

---

## Q & A :question:
Feel free to reach out with any questions or feedback!
