import json
import sys


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python ai/remediate.py <trivy-report.json>", file=sys.stderr)
        return 1

    with open(sys.argv[1], "r", encoding="utf-8") as file:
        report = json.load(file)

    for result in report.get("Results", []):
        for vulnerability in result.get("Vulnerabilities", [])[:10]:
            severity = vulnerability.get("Severity", "UNKNOWN")
            package = vulnerability.get("PkgName", "unknown")
            fixed_version = vulnerability.get("FixedVersion", "unavailable")
            print(f"[{severity}] {package} -> upgrade to {fixed_version}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
