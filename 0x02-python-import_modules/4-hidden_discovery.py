#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for word in dir(hidden_4):
        if word[0] == '_' and word[1] == '_':
            pass
        else:
            print(word)
