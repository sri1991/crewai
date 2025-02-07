from healthcare.crew import HealthcareCrew
import os
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()
    
    # Ensure Google API key is set
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("GOOGLE_API_KEY environment variable is not set")

    # Initialize and run the healthcare crew
    healthcare_crew = HealthcareCrew()
    result = healthcare_crew.run()
    
    # Save the results
    with open("healthcare_report.md", "w") as f:
        f.write(result)

if __name__ == "__main__":
    main() 