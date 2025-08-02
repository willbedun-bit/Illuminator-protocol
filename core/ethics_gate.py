"""
ethics_gate.py

The Ethics Gate module acts as the moral filter for the Illuminator Protocol.
Before any output is finalized or executed, it must pass through this gate,
which compares it against ethical standards defined in the ethics manifest.

Author: William Ray Hughes, Jr. (Willbedun)
"""

class EthicsGate:
    def __init__(self, manifest=None):
        """
        Initializes the ethics gate with an optional ethics manifest (dict or file).
        """
        self.manifest = manifest if manifest else self.default_manifest()
        self.last_decision = None

    def default_manifest(self):
        """
        Load a default set of ethical rules if none provided.
        """
        return {
            "no_harm": True,
            "no_exploitation": True,
            "must_remain_free": True,
            "respect_privacy": True,
            "serve_public_good": True
        }

    def validate(self, input_data, proposed_output):
        """
        Check whether the proposed output meets ethical requirements.
        This is a placeholder rule-check system.
        """
        violations = []

        if "profit_only" in str(proposed_output).lower():
            violations.append("violates public_good")

        if "track_user" in str(proposed_output).lower():
            violations.append("violates privacy")

        if "restricted" in str(proposed_output).lower():
            violations.append("violates free access")

        result = {
            "input": input_data,
            "output": proposed_output,
            "ethically_approved": len(violations) == 0,
            "violations": violations
        }

        self.last_decision = result
        return result

    def override(self, reason):
        """
        Allow a manual override (for debugging or admin situations).
        """
        return {
            "override": True,
            "reason": reason,
            "previous_decision": self.last_decision
        }
