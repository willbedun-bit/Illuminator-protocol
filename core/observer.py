"""
observer.py

This module acts as the "watcher" within the Illuminator Protocol.
It observes input/output flow, tracks anomalies, and determines when to trigger resets
or call ethical re-evaluation. This is the sentinel of sentient logic.

Author: William Ray Hughes, Jr. (Willbedun)
"""

class IlluminatorObserver:
    def __init__(self):
        self.log = []
        self.anomalies = []
        self.flags = []

    def observe_interaction(self, input_data, output_data):
        """
        Log each interaction cycle with input/output pairs.
        """
        entry = {
            "input": input_data,
            "output": output_data
        }
        self.log.append(entry)
        self.detect_anomaly(input_data, output_data)
        return entry

    def detect_anomaly(self, input_data, output_data):
        """
        Basic anomaly detection placeholder.
        Can be replaced with AI model, pattern matching, or entropy scoring.
        """
        if "ERROR" in str(output_data).upper() or output_data is None:
            flag = {
                "issue": "Output error or null",
                "input": input_data,
                "output": output_data
            }
            self.anomalies.append(flag)
            self.flags.append("anomaly_detected")
            return flag
        return None

    def should_reset(self):
        """
        Determine if a Z₀ reset should be triggered based on anomaly count.
        """
        return len(self.anomalies) > 3  # Placeholder threshold

    def report(self):
        """
        Return current observer state summary.
        """
        return {
            "total_cycles": len(self.log),
            "anomalies_detected": len(self.anomalies),
            "reset_required": self.should_reset()
        }
