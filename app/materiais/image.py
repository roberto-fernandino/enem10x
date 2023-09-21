from pathlib import Path

def define_image_path_questoes(instance, filename: str) -> str:
    """
    Define path para questoes que serao adcionadas.
    """
    return Path(f"questoes/{filename}")