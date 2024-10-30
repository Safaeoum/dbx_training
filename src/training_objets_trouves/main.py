from .utils.emails import get_initials


def main() -> None:
    username: str = "safae.oumami@capgemini.com"
    print(f"Hello from {get_initials(username)}")


if __name__ == "__main__":
    main()
