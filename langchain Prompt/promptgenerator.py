from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
    input_variables=["paper_name", "style", "length"],
    template="""Please summarize the research paper titled '{paper_name}' with the following specifications:
Explanation Style: {style}
Explanation Length: {length}

Mathematical Details:

Include relevant mathematical equations if present in the paper.

Explain the mathematical concepts using simple, intuitive code snippets where applicable.

Analogies:

Use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and length"""
)

prompt_template.save('prompt_template.json')