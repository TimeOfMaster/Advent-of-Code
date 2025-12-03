import "dart:io";

/// Read and parse input file
List<String> readInput(String filename) {
  return File(filename).readAsLinesSync();
}

/// TODO: Implement part 2 solution
dynamic solve(List<String> data) {
  // Your solution here
  return 0;
}

void main() {
  final scriptDir = File(Platform.script.toFilePath()).parent.path;
  final inputFile = "$scriptDir${Platform.pathSeparator}input.txt";
  final data = readInput(inputFile);

  print("Part 2: ${solve(data)}");
}
