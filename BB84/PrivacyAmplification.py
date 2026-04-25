def xor_compress(key: str) -> str:
    if len(key) < 2:
        return key
    result = []
    for i in range(0, len(key) - 1, 2):
        result.append(str(int(key[i]) ^ int(key[i + 1])))
    return "".join(result)