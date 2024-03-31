from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    AC_STRENGTH = 150
    MINIMUM_NEEDED_STRENGTH = 75

    def __init__(self, name: str):
        super().__init__(name, self.AC_STRENGTH)

    def can_climb(self):
        return self.strength >= self.MINIMUM_NEEDED_STRENGTH

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= 30 * 2.5
        elif peak.difficulty_level == "Advanced":
            self.strength -= 30 * 1.3

        self.conquered_peaks.append(peak.name)
