class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return False if (int(coordinates[1])%2!=0 and (coordinates[0]=='a' or coordinates[0]=='c' or coordinates[0]=='e' or coordinates[0]=='g')) or (int(coordinates[1])%2==0 and (coordinates[0]=='b' or coordinates[0]=='d' or coordinates[0]=='f' or coordinates[0]=='h')) else True