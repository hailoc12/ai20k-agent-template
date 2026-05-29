from langchain_core.tools import tool


@tool
def search_knowledge(query: str) -> str:
    """Tìm kiếm thông tin trong knowledge base.

    Args:
        query: Câu hỏi cần tìm kiếm

    Returns:
        Kết quả tìm kiếm
    """
    # TODO: Implement actual search logic
    return f"Kết quả tìm kiếm cho: {query}"


@tool
def calculate(expression: str) -> str:
    """Tính toán biểu thức toán học.

    Args:
        expression: Biểu thức cần tính

    Returns:
        Kết quả tính toán
    """
    try:
        result = eval(expression)  # noqa: S307 — chỉ demo
        return str(result)
    except Exception as e:
        return f"Lỗi tính toán: {e}"
