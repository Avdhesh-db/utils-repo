def get_greeting_message(name="World"):
    """
    Returns a simple greeting message.
    
    Args:
        name (str): The name to include in the greeting. Defaults to "World".
    
    Returns:
        str: A formatted greeting message.
    """
    return f"Hello, {name}! This message comes from the utils-repo in Databricks."


def say_goodbye(name="Friend"):
    """
    Returns a simple goodbye message.
    
    Args:
        name (str): The name to include in the goodbye. Defaults to "Friend".
    
    Returns:
        str: A formatted goodbye message.
    """
    return f"Goodbye, {name}! Databricks workflow completed successfully."
