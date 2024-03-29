from project.next_id_mixin import NextIdMixin


class ExercisePlan(NextIdMixin):
    id = 1
    minutes_in_hour = 60

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.get_next_id()
        self.increment_id()

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours * ExercisePlan.minutes_in_hour)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
