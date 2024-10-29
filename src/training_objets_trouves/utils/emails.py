def get_initials(email: str) -> str:
    """
    Return initials based on cluster creator
    Args:
        email (str): The email address from which to extract initials.
 
    Returns:
        str: A string of initials formed from the local part of the email.
    """
    name_part: str = email.split("@")[0]
    names: list[str] = name_part.split(".")
    initials: str = "".join([name[0] for name in names if name])
    return initials
