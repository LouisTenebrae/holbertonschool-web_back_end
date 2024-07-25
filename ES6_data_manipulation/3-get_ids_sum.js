export default function getStudentIdsSum(studentList) {
  return studentList.reduce(
    (acummulator, student) => acummulator + student.id, 0,
  );
}
