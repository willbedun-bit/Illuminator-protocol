"""
memory.py

This module handles memory persistence for the Illuminator Protocol.
Implements short-term and long-term memory logic, pruning strategies,
and prioritization of emotionally or ethically significant events.

Author: William Ray Hughes, Jr. (Willbedun)
"""

class MemoryManager:
    def __init__(self, memory_limit=100):
        """
        Initializes memory store with optional capacity for short-term memory.
        """
        self.short_term = []
        self.long_term = []
        self.memory_limit = memory_limit

    def store(self, interaction):
        """
        Stores an interaction in short-term memory and checks for significance.
        """
        self.short_term.append(interaction)
        if len(self.short_term) > self.memory_limit:
            self.short_term.pop(0)  # FIFO removal

        if self.is_significant(interaction):
            self.long_term.append(interaction)
            return "Stored in long-term memory"

        return "Stored in short-term memory"

    def is_significant(self, interaction):
        """
        Placeholder logic to determine memory importance.
        Can later use NLP scoring, anomaly detection, or ethical weight.
        """
        output = str(interaction.get("output", "")).lower()
        keywords = ["forgive", "love", "truth", "reset", "violation"]
        return any(kw in output for kw in keywords)

    def recall(self, query=None):
        """
        Retrieve memory entries matching a query.
        """
        if not query:
            return self.long_term[-5:]  # Return last 5 significant memories

        matches = [m for m in self.long_term if query.lower() in str(m).lower()]
        return matches

    def clear_short_term(self):
        """
        Clears the short-term memory buffer.
        """
        self.short_term = []

    def summarize(self):
        """
        Summarizes current memory state.
        """
        return {
            "short_term_count": len(self.short_term),
            "long_term_count": len(self.long_term)
        }
