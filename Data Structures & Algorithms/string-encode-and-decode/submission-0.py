class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded_str = ""
        for s in strs:
            word_length = len(s)
            encoded_str += str(word_length) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        decoded = []
        i = 0
        while i < len(s):
            # Find the '#' delimiter
            j = i
            while s[j] != "#":
                j += 1
            # Extract the length
            word_length = int(s[i:j])
            # Extract the word starting after '#' with the given length
            word = s[j + 1 : j + 1 + word_length]
            decoded.append(word)
            # Move index to the start of next encoded word
            i = j + 1 + word_length
        return decoded

