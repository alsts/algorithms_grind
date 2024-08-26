from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            word_len = int(s[i:j])
            i = j + 1  # beginning of word
            j = i + word_len  # end of word
            decoded.append(s[i:j])

            i = j

        return decoded

    def decode_str_modified(self, s: str) -> List[str]:
        decoded = []

        while len(s) > 0:
            c_count_offset = 0
            while c_count_offset < len(s) and s[c_count_offset].isdigit() and s[c_count_offset] != "#":
                c_count_offset += 1

            number_of_word_chars = int(s[0:c_count_offset])
            offset = 1 + c_count_offset
            # delimiter + word number chars (#1,#10,#100)
            decoded_s = s[offset: offset + number_of_word_chars]
            decoded.append(decoded_s)

            s = s[offset + number_of_word_chars:len(s)]

        return decoded

solution = Solution()
encoded = solution.encode(["we", "say", ":", "yes", "!@#$%^&*()"])
print(encoded)
decoded = solution.decode(encoded)
print(decoded)
