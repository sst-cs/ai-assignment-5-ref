"""
AI Assignment 05 — Tool-Calling Agent
Student implementation file.
"""

class Agent:
    """
    A tool-calling AI agent that solves structured data tasks.
    Mimics the architecture of modern LLM agents (LangChain, function-calling)
    with a deterministic planner.
    """

    def __init__(self, toolkit, datasets):
        """
        Args:
            toolkit: ToolKit instance (call tools via toolkit.call(name, **kw))
            datasets: dict of {"countries": [...], "products": [...]}
        """
        self.toolkit = toolkit
        self.datasets = datasets
        self.scratchpad = {}    # named intermediate results
        self.history = []       # execution log

    def plan(self, task):
        """
        Analyze a task and produce an execution plan.

        Must return a list of step dicts, each with:
            {"tool": str, "args": dict, "save_as": str}

        Rules:
        1. Read task["steps_hint"] for the ordered list of tool names needed
        2. For each tool in steps_hint, build the args dict from task["params"]
        3. The FIRST step that needs data should use: "data": "$dataset"
        4. Subsequent steps that need previous result use: "data": "$<save_as>"
        5. If a param value is "$agg_result" or starts with "$", it means
           "use the result of the step that was saved with that key"
        6. The last step's save_as must be "result"
        7. If steps_hint mentions a target_field, add a final get_field step

        Raises ValueError if task is missing required params.
        """
        # TODO: Implement this method
        pass

    def execute(self, plan, task):
        """
        Execute the plan step by step.

        For each step:
        1. Resolve "$" references in args
        2. Call self.toolkit.call(step["tool"], **resolved_args)
        3. Store result in self.scratchpad[step["save_as"]]
        4. Log to self.history: {"tool": ..., "args": ..., "result": ..., "success": True}
        5. If ToolError raised: store None, log success=False, continue

        Returns: bool (True if ALL steps succeeded, False if any failed)
        """
        # TODO: Implement this method
        pass

    def get_answer(self, task):
        """
        Extract the final answer from the scratchpad.

        1. Get self.scratchpad.get("result")
        2. Format based on task["answer_type"]:
           - "string", "number" (round 2 decimal), "integer", "boolean"
           - "list": extract target_field from each dict
        3. If result is None, return None
        """
        # TODO: Implement this method
        pass

    def solve(self, task):
        """
        Full agent pipeline:
        1. Reset scratchpad and history
        2. plan = self.plan(task)
        3. success = self.execute(plan, task)
        4. answer = self.get_answer(task)
        5. Return answer
        """
        # TODO: Implement this method
        pass

    def solve_batch(self, tasks):
        """
        Solve multiple tasks independently.
        Returns dict: {task["id"]: answer}
        """
        # TODO: Implement this method
        pass
