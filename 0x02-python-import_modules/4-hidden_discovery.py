#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as module
    module_names = dir(module)
    for module_name in module_names:
        if module_name[:2] != "__":
            print(module_name)
