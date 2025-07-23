# pyright: reportPrivateImportUsage=false
import google.generativeai as genai

# ✅ Configure the Gemini API key (use your own here securely in production)
genai.configure(api_key="AIzaSyA9ItiUpO-kZGBsI4XT5upiIcTuTPt0TvU")

# ✅ Table schema for your E-commerce dataset
SCHEMA_INFO = """
Table: Ad_Sales_Metrics (Date, Campaign, Clicks, Spend, Revenue)
Table: Total_Sales_Metrics (Date, Category, Units_Sold, Total_Revenue)
Table: Eligibility_Table (ProductID, Category, Is_Eligible_For_Discount)
"""

# ✅ Function to convert question to SQL
def question_to_sql(question: str) -> str:
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    prompt = f"""
    Based on the table schema below, write a standard SQL query that answers the user's question.
    Only return the SQL query and nothing else.

    Schema:
    {SCHEMA_INFO}

    Question:
    {question}

    SQL Query:
    """
    response = model.generate_content(prompt)
    return response.text.strip().replace("`", "").replace("sql", "")

# ✅ Function to convert SQL result into human-readable answer
def answer_in_sentence(question: str, query_result: str) -> str:
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    prompt = f"""
    You are a helpful sales analyst. Your user asked the following question:
    "{question}"

    You ran a query and got the following result:
    "{query_result}"

    Based on the result, provide a short, natural language answer to the user's question.
    Summarize the key insight. Do not mention the query.
    """
    response = model.generate_content(prompt)
    return response.text.strip()

# ✅ Test block to verify agent behavior
if __name__ == "__main__":
    question = "What is the total revenue for electronics in June?"
    print("🧠 Original Question:")
    print(question)

    sql_query = question_to_sql(question)
    print("\n🧾 Generated SQL Query:")
    print(sql_query)

    # Simulate a query result from DB (replace this later with real DB call)
    dummy_result = "The total revenue for electronics in June was $12,450."
    
    final_answer = answer_in_sentence(question, dummy_result)
    print("\n💡 AI Final Answer:")
    print(final_answer)
