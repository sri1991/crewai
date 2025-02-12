from crewai import Agent, Task, Crew
from typing import Dict
import yaml
from pathlib import Path
import os
import google.generativeai as genai
from .tools.tool_manager import ToolManager

class HealthcareCrew:
    def __init__(self):
        self.config_path = Path(__file__).parent / "config"
        # Configure Gemini
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel('gemini-1.5-pro')
        self.tool_manager = ToolManager()
        self.agents = self._load_agents()
        self.tasks = self._load_tasks()

    def _load_agents(self) -> Dict[str, Agent]:
        """Load agent configurations and create Agent instances"""
        with open(self.config_path / "agents.yaml", "r") as file:
            agents_config = yaml.safe_load(file)

        agents = {}
        for agent_id, config in agents_config.items():
            tools = self.tool_manager.get_tools(config["tools"])
            agents[agent_id] = Agent(
                name=config["name"],
                role=config["role"],
                goal=config["goal"],
                backstory=config["backstory"],
                verbose=config["verbose"],
                allow_delegation=True,
                tools=tools,
                llm=self.model
            )
        return agents

    def _load_tasks(self) -> list[Task]:
        """Load task configurations and create Task instances"""
        with open(self.config_path / "tasks.yaml", "r") as file:
            tasks_config = yaml.safe_load(file)

        tasks = []
        for category in tasks_config.values():
            for task_config in category:
                tasks.append(Task(
                    description=task_config["description"],
                    agent=self.agents[task_config["agent"]],
                    expected_output=task_config["expected_output"]
                ))
        return tasks

    def _get_tools(self, tool_names: list) -> list:
        """Load and return tools based on tool names"""
        # Implement tool loading logic here
        return []

    def run(self) -> str:
        """Execute the healthcare management workflow"""
        crew = Crew(
            agents=list(self.agents.values()),
            tasks=self.tasks,
            verbose=True
        )
        result = crew.kickoff()
        return result 