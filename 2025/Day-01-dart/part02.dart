import 'dart:io';

/// Read and parse input file
List<String> readInput(String filename) {
  return File(filename).readAsLinesSync();
}

(int, int) dial(String instruction, int position, {int dialSize = 100}) {
  String direction = instruction[0];
  int distance = int.parse(instruction.substring(1));
  int hits = 0;
  int new_position = 0;

  if (direction == "R") {
    for (int i = 1; i <= distance; i++) {
      new_position = (position + i) % dialSize;
      if (new_position == 0) {
        hits += 1;
      }
    }
    position = new_position;
  } else if (direction == "L") {
    for (int i = 1; i <= distance; i++) {
      new_position = (position - i) % dialSize;
      if (new_position == 0) {
        hits += 1;
      }
    }
    position = new_position;
  }

  return (position, hits);
}

int solve(List<String> data) {
  int position = 50;
  int hits = 0;

  for (String instruction in data) {
    int hits_on_dial;
    (position, hits_on_dial) = dial(instruction, position);
    hits += hits_on_dial;
  }
  return hits;
}

void main() {
  final scriptDir = File(Platform.script.toFilePath()).parent.path;
  final inputFile = '$scriptDir${Platform.pathSeparator}input.txt';
  final data = readInput(inputFile);

  print("Part 2: ${solve(data)}");
}
