"""Post-generation validation hook for copier-python-template."""

import re
import sys


def validate_package_name(package_name: str) -> None:
    """Validate that package_name is a valid Python identifier.

    Args:
        package_name: The package name to validate.

    Raises:
        SystemExit: If package_name is not a valid Python identifier.
    """
    pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    if not re.match(pattern, package_name):
        print(
            f"ERROR: package_name '{package_name}' is not a valid Python identifier.\n"
            f"Use underscores, not hyphens (e.g. 'my_package', not 'my-package').",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "validate":
        validate_package_name(sys.argv[2])
