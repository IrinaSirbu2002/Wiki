import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries(types):
    """
    Returns a list of all names of encyclopedia entries.
    """
    if types is None:
        types = [""]  # Default to searching in the root "entries" folder

    entries = []
    for type in types:
        _, filenames = default_storage.listdir(f"entries/{type}")
        entries.extend(sorted(re.sub(r"\.md$", "", filename) for filename in filenames if filename.endswith(".md")))

    return entries

def list_entries_by_type(type):
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir(f"entries/{type}")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content, type):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{type}/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title, types):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    if types is None:
        types = list_entries()  # List all available folders

    for type in types:
        try:
            f = default_storage.open(f"entries/{type}/{title}.md")
            return f.read().decode("utf-8")
        except FileNotFoundError:
            continue  # Move to the next folder

    return None 