class Solution:
    def convertDateToBinary(self, date: str) -> str:
        YYYY,MM,DD = date.split("-")
        YYYY=bin(int(YYYY))[2:]
        MM=bin(int(MM))[2:]
        DD=bin(int(DD))[2:]
        return f"{YYYY}-{MM}-{DD}"