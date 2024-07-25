export default function getListStudentIds(listObjects) {
  if (!Array.isArray(listObjects)) {
    return [];
  }
  return listObjects.map((student) => student.id);
}
