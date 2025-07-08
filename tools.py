import logging
from livekit.agents import function_tool, RunContext
import requests
from langchain_community.tools import DuckDuckGoSearchRun

@function_tool()
async def search_web(query: str, run_context: RunContext) -> str:
    """
    Search the web using DuckDuckGo and return the first result.
    """
    try:
        results = DuckDuckGoSearchRun().run(tool_input=query)
        logging.info(f"Web search results for '{query}': {results}")
        return results if results else "No results found."
    except Exception as e:
        logging.error(f"Error during web search: {e}")
        return "An error occurred while searching the web."

# @function_tool()
# async def send_email(context: RunContext, to_email: str, subject: str, message: str) -> str:
#     """
#     Send an email through Gmail SMTP.

#     Args:
#         context (RunContext): The run context for logging.
#         to_email (str): The recipient's email address.
#         subject (str): The subject of the email.
#         message (str): The body of the email.
#     """
#     try:
#         import smtplib
#         from email.mime.text import MIMEText

#         msg = MIMEText(body)
#         msg['Subject'] = subject
#         msg['From'] = '
