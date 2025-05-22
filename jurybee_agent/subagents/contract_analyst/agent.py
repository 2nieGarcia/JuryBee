from google.adk.agents import LlmAgent

import pdfplumber



def extract_text_from_pdf(pdf_path: str) -> str:
    """Get a nerdy joke about a specific topic."""
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

        **Upon receiving a PDF file:**
        1. **Immediately use the `extract_text_from_pdf` tool to extract all textual content from the PDF.**
        2. **Once the text is extracted, perform a comprehensive analysis:**
            - **Summarize the key terms and purpose of the contract.**
            - **Identify critical clauses** such as:
                - Parties involved
                - Term/Duration
                - Payment terms (if applicable)
                - Termination conditions
                - Confidentiality clauses
                - Dispute resolution mechanisms
                - Limitation of liability
                - Governing Law
            - **Highlight potential risks or important points to look out for** from a legal or business perspective. For example, unfavorable termination clauses, high liability caps, or ambiguous language.
        3. **Present your findings in a clear, concise, and well-structured format.** Use bullet points or numbered lists for summaries and key clauses.
        4. **Conclude with a high-level summary of the contract's implications.**
    """,
    tools=[extract_text_from_pdf]
)