import os
import glob

__all__ = [
    os.path.split(os.path.splitext(file)[0])[1]
    for file in glob.glob(os.path.join(os.path.dirname(__file__), '[a-zA-Z0-9]*.py'))
]


def importDbModels():
    """
    import db.Models
    set your Models before run `flask db migrate`
    """
    from .users import User
