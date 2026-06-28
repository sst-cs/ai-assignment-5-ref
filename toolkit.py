"""
AI Assignment 05 — Toolkit
Provides 6 tool functions and the ToolKit registry class.
DO NOT MODIFY THIS FILE.
"""


class ToolError(Exception):
    """Raised when a tool call fails."""
    pass


def search(data, field, value):
    """
    Find all records where record[field] == value (case-insensitive for strings).

    Args:
        data:  list of dicts
        field: string — key to check
        value: the value to match

    Returns:
        list of dicts that match
    """
    if not isinstance(data, list):
        raise ToolError(f"search: 'data' must be a list, got {type(data).__name__}")
    if not data:
        return []
    if field not in data[0]:
        raise ToolError(f"search: field '{field}' not found in data")
    results = []
    for record in data:
        v = record.get(field)
        if isinstance(v, str) and isinstance(value, str):
            if v.lower() == value.lower():
                results.append(record)
        elif v == value:
            results.append(record)
    return results


def filter_records(data, field, operator, value):
    """
    Filter records using a comparison operator.

    Args:
        data:     list of dicts
        field:    string — key to compare
        operator: one of 'eq', 'neq', 'gt', 'lt', 'gte', 'lte', 'contains'
        value:    comparison value

    Returns:
        list of dicts that pass the filter
    """
    if not isinstance(data, list):
        raise ToolError(f"filter_records: 'data' must be a list, got {type(data).__name__}")
    if not data:
        return []
    if field not in data[0]:
        raise ToolError(f"filter_records: field '{field}' not found in data")

    ops = {
        'eq':       lambda a, b: a == b,
        'neq':      lambda a, b: a != b,
        'gt':       lambda a, b: a > b,
        'lt':       lambda a, b: a < b,
        'gte':      lambda a, b: a >= b,
        'lte':      lambda a, b: a <= b,
        'contains': lambda a, b: isinstance(a, str) and b.lower() in a.lower(),
    }
    if operator not in ops:
        raise ToolError(f"filter_records: unknown operator '{operator}'. Use one of {list(ops.keys())}")

    fn = ops[operator]
    return [r for r in data if fn(r.get(field), value)]


def sort_records(data, field, ascending=True):
    """
    Sort a list of dicts by a field.

    Args:
        data:      list of dicts
        field:     string — key to sort by
        ascending: bool

    Returns:
        new sorted list (original unchanged)
    """
    if not isinstance(data, list):
        raise ToolError(f"sort_records: 'data' must be a list, got {type(data).__name__}")
    if not data:
        return []
    if field not in data[0]:
        raise ToolError(f"sort_records: field '{field}' not found in data")
    return sorted(data, key=lambda r: r[field], reverse=not ascending)


def aggregate(data, field, operation):
    """
    Aggregate a numeric field across records.

    Args:
        data:      list of dicts
        field:     string — key to aggregate
        operation: one of 'sum', 'mean', 'min', 'max', 'count'

    Returns:
        float result
    """
    if not isinstance(data, list):
        raise ToolError(f"aggregate: 'data' must be a list, got {type(data).__name__}")
    if not data:
        raise ToolError("aggregate: empty data — cannot aggregate")
    if field not in data[0]:
        raise ToolError(f"aggregate: field '{field}' not found in data")

    values = [r[field] for r in data if r[field] is not None]
    if not values:
        raise ToolError(f"aggregate: no non-None values for field '{field}'")

    if operation == 'sum':
        return float(sum(values))
    elif operation == 'mean':
        return float(sum(values) / len(values))
    elif operation == 'min':
        return float(min(values))
    elif operation == 'max':
        return float(max(values))
    elif operation == 'count':
        return float(len(values))
    else:
        raise ToolError(f"aggregate: unknown operation '{operation}'. Use sum/mean/min/max/count")


def get_field(data, field, index=0):
    """
    Extract a single field value from a record.

    If data is a list of dicts, return data[index][field].
    If data is a single dict, return data[field].
    If data is a number/string (scalar), return data.

    Args:
        data:  list of dicts, a single dict, or a scalar
        field: string — key to extract
        index: int — which record (default 0, i.e. first)

    Returns:
        the extracted value
    """
    if isinstance(data, (int, float, str, bool)):
        return data  # already a scalar
    if isinstance(data, dict):
        if field not in data:
            raise ToolError(f"get_field: field '{field}' not found in record")
        return data[field]
    if isinstance(data, list):
        if not data:
            raise ToolError("get_field: empty data list")
        if index >= len(data):
            raise ToolError(f"get_field: index {index} out of range (len={len(data)})")
        record = data[index]
        if isinstance(record, dict):
            if field not in record:
                raise ToolError(f"get_field: field '{field}' not found in record")
            return record[field]
        return record
    raise ToolError(f"get_field: unexpected data type {type(data).__name__}")


def calculate(expression):
    """
    Safely evaluate a math expression string.

    Supports: +, -, *, /, //, **, %, (), round(), abs(), min(), max()
    Example: calculate('round(1234567 / 1000000, 2)') -> 1.23

    Args:
        expression: string math expression

    Returns:
        float result
    """
    allowed_names = {
        'round': round, 'abs': abs, 'min': min, 'max': max,
        'int': int, 'float': float,
    }
    try:
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return float(result)
    except Exception as e:
        raise ToolError(f"calculate: failed to evaluate '{expression}': {e}")


class ToolKit:
    """Registry of tools the agent can call."""

    def __init__(self):
        self._tools = {}
        # Register all default tools
        for fn in [search, filter_records, sort_records, aggregate, get_field, calculate]:
            self._tools[fn.__name__] = {
                'function': fn,
                'doc': fn.__doc__,
            }

    def call(self, tool_name, **kwargs):
        """
        Call a registered tool by name.

        Args:
            tool_name: string — name of the tool
            **kwargs:  arguments to pass to the tool

        Returns:
            the tool's return value

        Raises:
            ToolError if tool not found or tool execution fails
        """
        if tool_name not in self._tools:
            raise ToolError(f"ToolKit: unknown tool '{tool_name}'. Available: {list(self._tools.keys())}")
        try:
            return self._tools[tool_name]['function'](**kwargs)
        except ToolError:
            raise
        except Exception as e:
            raise ToolError(f"ToolKit: tool '{tool_name}' failed: {e}")

    def list_tools(self):
        """Return list of (name, docstring) for all registered tools."""
        return [(name, info['doc']) for name, info in self._tools.items()]
