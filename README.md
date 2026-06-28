# AI Assignment 05: Tool-Calling Agent

In this assignment, you will build a deterministic planner for a tool-calling AI agent. You are given a `ToolKit` with 6 tools and a set of 20 tasks to solve against two knowledge bases (`countries` and `products`).

Your goal is to implement the `Agent` class in `agent.py` to match the architecture of modern LLM agents (like LangChain or OpenAI function calling) — but instead of a neural network, your planner will use rule-based logic to map task hints to a sequence of tool calls.

## How It Works

A task looks like this:
```python
{
    "id": "T01",
    "dataset": "countries",
    "goal": "Find the capital of France",
    "steps_hint": ["search", "get_field"],
    "params": {
        "search_field": "name", 
        "search_value": "France",
        "target_field": "capital"
    },
    "answer_type": "string"
}
```

The agent must:
1. **Plan:** Read `steps_hint` and `params` to generate a list of tool steps with correct arguments.
2. **Execute:** Call the tools via `self.toolkit.call(tool_name, **args)` and save intermediate results in `self.scratchpad`.
3. **Get Answer:** Extract and format the final result.

## The Scratchpad and $ References

The `scratchpad` is the agent's working memory. 
- The FIRST step that needs data must pass `data: "$dataset"`. `execute()` should replace this with `self.datasets[task["dataset"]]`.
- When a step is executed, its result is saved in the scratchpad under its `save_as` name.
- Subsequent steps reference previous results using `$`. For example, if a parameter value is `"$agg_result"`, it means "look up the value of `agg_result` in the scratchpad and use it here."
- The final step's output must be saved as `"result"`.

## Available Tools

Do not modify `toolkit.py`. The available tools are:
- `search(data, field, value)`
- `filter_records(data, field, operator, value)`
- `sort_records(data, field, ascending)`
- `aggregate(data, field, operation)`
- `get_field(data, field, index)`
- `calculate(expression)`

## To Run Locally
`python main.py`

## Submission
Push to GitHub Classroom to trigger the autograder.
