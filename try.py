import pandas as pd
from crewai import Agent, Task, Crew
from typing import Dict
from langchain.tools import BaseTool

class ExcelToTextTool(BaseTool):
    name = "excel_to_text_converter"
    description = "Converts Excel file content to text format"
    
    def _run(self, excel_path: str) -> str:
        """Convert Excel file content to text format."""
        try:
            # Read Excel file
            df = pd.read_excel(excel_path)
            
            # Convert DataFrame to text
            text_content = []
            for column in df.columns:
                text_content.append(f"\n{column}:")
                text_content.extend(df[column].astype(str).tolist())
            
            return "\n".join(text_content)
        except Exception as e:
            return f"Error processing Excel file: {str(e)}"

    def _arun(self, excel_path: str) -> str:
        """Async implementation of the tool."""
        # For simplicity, we'll use the sync version
        return self._run(excel_path)

# Create an agent with the custom tool
classifier_agent = Agent(
    role='Document Classifier',
    goal='Accurately classify documents into appropriate categories',
    backstory="""You are an expert document classifier with deep understanding
                of various document types and categories.""",
    tools=[ExcelToTextTool()],
    verbose=True
)

# Create a task for document classification
def create_classification_task(excel_path: str) -> Task:
    return Task(
        description=f"""
        1. Use the excel_to_text_converter tool to convert the Excel file at {excel_path} to text
        2. Analyze the converted text content
        3. Classify the document into one of the following categories:
           - Financial Report
           - Technical Documentation
           - Marketing Material
           - Legal Document
           - Other (specify)
        4. Provide a brief explanation for the classification
        """,
        agent=classifier_agent
    )

# Example usage
def main():
    # Create the crew
    crew = Crew(
        agents=[classifier_agent],
        tasks=[create_classification_task("path/to/your/excel_file.xlsx")]
    )
    
    # Execute the task
    result = crew.kickoff()
    return result

# Example of how to use the implementation
if __name__ == "__main__":
    # Sample code to test the implementation
    test_data = {
        'Title': ['Q4 Financial Report'],
        'Content': ['Revenue increased by 15% compared to Q3...'],
        'Date': ['2024-01-15']
    }
    
    # Create a sample Excel file
    df = pd.DataFrame(test_data)
    test_file = "test_document.xlsx"
    df.to_excel(test_file, index=False)
    
    # Run the classification
    result = main()
    print("Classification Result:", result)