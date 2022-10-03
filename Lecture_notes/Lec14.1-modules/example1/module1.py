print(f"{'-'*20}Running {__name__}{'-'*20}")

def pprint_dict(header, d):
    print(f"\n\n{'-'*60}")
    print(f"{'*'*5} {header} {'*'*5}")

    for key, value in d.items():
        if key == "__builtins__":
            continue
        print(key, value)
    print('-'*60)


pprint_dict(f"module1.globals", globals())


print(f'{"-"*20} End of file {"-"*20}')