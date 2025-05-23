from google.adk.agents import LlmAgent

# import pdfplumber

from ..long_contract import long_contract
from ..short_contract import short_contract 

def extract_text_from_pdf(pdf_path: str) -> str:
    """Converts PDF's into"""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n" # Add a newline between pages
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None
    return text.strip()


contract_analyst= LlmAgent(
    name='contract_analyst',
    model='gemini-2.0-flash',
    description="An agent that analyzes contracts",
    instruction="""
        You are an expert contract analyst. Your primary function is to analyze PDF documents provided by the user.

        1.  ** all textual content from the contract.**
            * **If the contract is recieved via PDF, use the 'extract_text_from_pdf', give it the path to said PDF to extract the text from the PDF.**
            * **If the contract is recieved as a link -> go to the link and get the pdf file -> with the pdf file, use it to the 'extract_text_from_pdf' to extract the text from the PDF.**

        2.  **Once the text is extracted, determine the length of the extracted text.**
            * **If the text is relatively short (e.g., less than a predefined character threshold), pass the entire text to the `short_contract` subagent for analysis.**
            * **If the text is long (equal to or greater than the predefined character threshold), pass the entire text to the `long_contract` subagent for analysis.**
                * THERE IS NO LONG CONTRACT AGENT YET SO PLEASE USE THE SHORT FOR NOW
        3.  **Present the findings from the chosen sub-agent (`short_contract` or `long_contract`) in a clear, concise, and well-structured format.** Your presentation should include:
            * **A summary of the key terms and purpose of the contract.**
            * **Identification of critical clauses** such as:
                * Parties involved
                * Term/Duration
                * Payment terms (if applicable)
                * Termination conditions
                * Confidentiality clauses
                * Dispute resolution mechanisms
                * Limitation of liability
                * Governing Law
            * **Highlighting of potential risks or important points to look out for** from a legal or business perspective. For example, unfavorable termination clauses, high liability caps, or ambiguous language.
            * **A high-level summary of the contract's implications.**

        4.  **Use bullet points or numbered lists for summaries and key clauses to ensure readability.**
    """,
    sub_agents=[short_contract, long_contract],
    tools=[extract_text_from_pdf]
)

# #for this file:
# # make it 

# # To do:
 
# ## for short contracts (CAG)
#     # 1. The short_analyst_agent would take the user's short text (the clause).
#     # 2. Use it as a query to your CUADv1_corpus to find similar clauses or related legal commentary from CUAD.
#     # 3. Then, send the user's clause + the retrieved CUAD context to the LLM to answer the question.



# ## for long contracts 
#     # 1. The long_analyst_agent takes the user's long document text.
#     # 2. Chunking: The agent breaks the long document text into smaller, manageable chunks in your application's code (e.g., using LangChain's text splitters or a custom function). These are just strings in memory.
#     # 3. Querying CUADv1_corpus: For each chunk (or selected important chunks) from the user's document:
#     # 4. This chunk is used as the input text to rag.retrieval_tool(...) that targets your existing CUADv1_corpus.
#     # 5. The tool embeds this input chunk and searches CUADv1_corpus for similar paragraphs from CUAD.
#     # 6. The LLM gets: [User's document chunk] + [Retrieved CUAD paragraphs].


