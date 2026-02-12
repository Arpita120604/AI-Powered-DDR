from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from utils import read_text

# Load environment variables
load_dotenv()

# Initialize LLM (model chosen for broad availability)
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Prompt template (strict, no hallucination)
prompt = PromptTemplate(
    input_variables=["inspection", "thermal"],
    template="""
You are an expert property diagnostic assistant.

Using ONLY the information provided below, generate a Detailed Diagnostic Report (DDR).
Do NOT assume or invent missing information.
If data is missing, clearly mention "Not Available".

Inspection Report:
{inspection}

Thermal Report:
{thermal}

Generate the DDR with the following sections:
1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment
5. Recommended Actions
6. Missing or Unclear Information
"""
)

def generate_ddr_ai(inspection_text, thermal_text):
    response = llm.invoke(
        prompt.format(
            inspection=inspection_text,
            thermal=thermal_text
        )
    )
    return response.content


if __name__ == "__main__":
    inspection_text = read_text("data/inspection_report.txt")
    thermal_text = read_text("data/thermal_report.txt")

    ddr_output = generate_ddr_ai(inspection_text, thermal_text)
    print(ddr_output)
