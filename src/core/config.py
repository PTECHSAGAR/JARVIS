"""
config.py - Handles application configuration and environment variables.
"""
import os

# TODO: Load and parse configurations.
class Config:
    def __init__(self):
        self.ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.model = os.getenv("OLLAMA_MODEL", "llama3")
        self.db_url = os.getenv("DATABASE_URL", "sqlite:///data/jarvis.db")
