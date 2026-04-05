class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return f"{chr(258)}"

        return f"{chr(257)}".join(strs)

    def decode(self, s: str) -> List[str]:

        if s == chr(258):
            return []

        return s.split(f"{chr(257)}")