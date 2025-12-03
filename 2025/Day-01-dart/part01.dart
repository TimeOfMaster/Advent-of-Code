import 'dart:io';

/// Read and parse input file
List<String> readInput(String filename) {
  return File(filename).readAsLinesSync();
}

int dial(String instruction, int position, {int dialSize = 100}) {
  String direction = instruction[0];
  int distance = int.parse(instruction.substring(1));

  if (direction == "L") {
    position = (position - distance) % dialSize;
  } else if (direction == "R") {
    position = (position + distance) % dialSize;
  }
  return position;
}

int solve(List<String> data) {
  int position = 50;
  int hits = 0;

  for (String instruction in data) {
    position = dial(instruction, position);
    if (position == 0) {
      hits += 1;
    }
  }
  return hits;
}

void main() {
  final scriptDir = File(Platform.script.toFilePath()).parent.path;
  final inputFile = '$scriptDir${Platform.pathSeparator}input.txt';
  final data = readInput(inputFile);

  print("Part 1: ${solve(data)}");
}
