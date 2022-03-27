import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Converts teradata script")
    parser.add_argument(
        "--script_path",
        metavar="path",
        required=True,
        help="the path to the teradata script",
    )
    parser.add_argument(
        "--sql_style",
        metavar="str",
        required=True,
        default="bigquery",
        help="where to run the sql script",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    print(args.script_path)
    print(args.sql_style)


if __name__ == "__main__":
    main()
