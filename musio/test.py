def test():
    import importlib
    return importlib.import_module('.all_file', 'musio')
print("Loaded")
