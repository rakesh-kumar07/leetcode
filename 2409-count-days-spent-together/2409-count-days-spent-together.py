class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day(date_str: str) -> int:
            month, day = map(int, date_str.split("-"))
            # Sum up days of previous months + current day
            return sum(days_in_months[:month - 1]) + day
        
        alice_start = date_to_day(arriveAlice)
        alice_end = date_to_day(leaveAlice)
        bob_start = date_to_day(arriveBob)
        bob_end = date_to_day(leaveBob)
        
        # Find the intersection of the two date ranges
        overlap_start = max(alice_start, bob_start)
        overlap_end = min(alice_end, bob_end)
        
        # Calculate overlapping days if valid
        if overlap_start <= overlap_end:
            return overlap_end - overlap_start + 1
        
        return 0