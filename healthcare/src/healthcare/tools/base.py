from typing import Any
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class HealthcareTool(BaseTool):
    """Base class for healthcare tools"""
    def __init__(self):
        super().__init__() 