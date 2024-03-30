from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("Ivan", {})
        self.student_with_course = Student("Petar", {"English": ["Manchester United"]})

    def test__init__(self):
        self.assertEqual("Ivan", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_enroll_add_new_notes_to_existing_course(self):
        result = self.student_with_course.enroll("English", "Chelsea", '')
        expected_result = "Course already added. Notes have been updated."
        self.assertEqual(expected_result, result)

    def test_enroll_notes_to_existing_course_without_third_param(self):
        result = self.student.enroll("French", "Chelsea", )
        expected_result = "Course and course notes have been added."
        self.assertEqual(expected_result, result)

    def test_enroll_notes_to_existing_course_with_third_param_Y(self):
        result = self.student.enroll("French", "Chelsea", "Y")
        expected_result = "Course and course notes have been added."
        self.assertEqual(expected_result, result)

    def test_enroll_add_new_course_without_notes(self):
        result = self.student.enroll("French", ["Lyon"], "n")
        self.assertEqual("Course has been added.", result)
        self.assertEqual({"French": []}, self.student.courses)

    def test_add_notes_to_existing_course(self):
        result = self.student_with_course.add_notes("English", "Chelsea")
        expected_result = "Notes have been updated"
        self.assertEqual(expected_result, result)

    def test_add_notest_to_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("French", "Lyon")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        result = self.student_with_course.leave_course("English")
        expected_result = "Course has been removed"
        self.assertEqual(expected_result, result)

    def test_leave_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("French")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
