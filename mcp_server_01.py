from fastmcp import FastMCP

mcp = FastMCP("🚀 MyFirstMCPServer")

@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool
def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b

# @mcp.tool
# def multiply(a: float, b: float) -> float:
#     """Multiply two numbers."""
#     return a * b

@mcp.tool
def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@mcp.tool
def power(a: float, b: float) -> float:
    """Raise a number to the power of another number."""
    return a ** b

@mcp.tool
def fraction(number: float) -> float:
    """Return 1 divided by the number. For example, 12.5 returns 0.08."""
    if number == 0:
        raise ValueError("Cannot divide by zero.")
    return 1 / number

if __name__ == "__main__":
    mcp.run(transport="sse", host="127.0.0.1", port=8000)