import nbformat
import sys

for nb_path in sys.argv[1:]:
    nb = nbformat.read(nb_path, as_version=4)
    widgets = nb.metadata.get("widgets", None)

    if isinstance(widgets, dict) and "state" not in widgets:
        widgets["state"] = {}
        nb.metadata["widgets"] = widgets
        nbformat.write(nb, nb_path)
        print(f"✅ Patched: {nb_path}")
    else:
        print(f"⚠️ No patch needed: {nb_path}")
