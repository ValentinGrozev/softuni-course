from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    AC_STRENGTH = 200
    MINIMUM_NEEDED_STRENGTH = 100

    def __init__(self, name: str):
        super().__init__(name, self.AC_STRENGTH)

    def can_climb(self):
        return self.strength >= self.MINIMUM_NEEDED_STRENGTH

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= 20 * 2
        elif peak.difficulty_level == "Advanced":
            self.strength -= 20 * 1.5

        self.conquered_peaks.append(peak.name)
