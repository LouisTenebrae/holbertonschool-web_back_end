export default function createInt8TypedArray(length, position, value) {
  // Create a new ArrayBuffer with the specified length
  const buffer = new ArrayBuffer(length);

  // Create an Int8Array view to manipulate the buffer
  const int8View = new Int8Array(buffer);

  // Check if the provided position is within the range of the buffer
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Check if the provided value is within the range of Int8
  if (value < -128 || value > 127) {
    throw new Error('Value outside range for Int8');
  }

  // Set the Int8 value at the specified position
  int8View[position] = value;

  // Return the populated ArrayBuffer
  return new DataView(buffer);
}
