import "package:test/test.dart";
import "part01.dart" as part01;
import "part02.dart" as part02;

void main() {
  group("Part 01", () {
    test("example test", () {
      List<String> exampleData = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82"
      ];
      expect(part01.solve(exampleData), equals(3));
    });
  });

  group("Part 02", () {
    test("example test", () {
      List<String> exampleData = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82"
      ];
      expect(part02.solve(exampleData), equals(6));
    });
  });
}
