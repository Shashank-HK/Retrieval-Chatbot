# Retrieval-Chatbot
Retrieval Chatbot using LSTMs (Keras)
A retrieval chatbot. Knowledge base consists of question-answer pairs. User query is first categorized based on intent using LSTM.
The query is then compared to find most similar question in the knowledge base, and the corresponding answer is displayed.

Steps to run - 
1. Run /script/get_response.py (Listen on TCP socket)
2. "npm start" in /backend folder to start node server
3. "npm start" in /frontend folder to start frontend
