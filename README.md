# E-commerce AI Sales Agent 🤖

This project is a conversational chatbot that allows users to ask natural language questions about e-commerce sales data. Using Google's Gemini API, the agent dynamically generates SQL queries, retrieves results from a local SQLite database, and presents answers in an interactive format with tables, charts, and natural language summaries.
<img width="1919" height="842" alt="image" src="https://github.com/user-attachments/assets/49e3c90c-8ef6-4ae1-a594-4819856ed7ef" />


## Features ✨

* **Natural Language Queries**: Ask complex questions like "What was our total revenue last week?" or "Which campaign had the most clicks?"
* **Dynamic SQL Generation**: Converts user questions into SQL queries in real-time.
* **Interactive UI**: Built with Streamlit to provide a user-friendly chat interface.
* **Data Visualization**: Automatically generates tables and bar charts to visualize the query results.
* **Local Database**: Uses a local SQLite database, making it easy to set up and run anywhere.

---

## Project Structure 📁
* `chatbot_app.py`: The main Streamlit application that powers the web interface.
* `gemini_agent.py`: Contains functions that interact with the Gemini API for SQL generation and text summarization.
* `query_engine.py`: Executes the generated SQL queries on the SQLite database.
* `csvtosql.py`: A one-time script to load data from CSV files into the `sales.db` SQLite database.
* `test_llm.py`: A command-line script for testing the backend logic without the UI.
* `requirements.txt`: A list of all the Python libraries required for the project.
* `*.csv`: Raw data files.

---
## 📊 Datasets Used
Product-Level Ad Sales and Metrics
Product-Level Total Sales and Metrics
Product-Level Eligibility Table

---
### Sample Questions
What is my total sales?
Calculate the RoAS (Return on Ad Spend).
Which product had the highest CPC (Cost Per Click)?

---

### Demo Video
https://drive.google.com/file/d/1PTfBj3MIQo4g5HsS2siJz_yV-jyNL1mo/view?usp=sharing
