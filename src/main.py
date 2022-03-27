import argparse
from pathlib import Path
import bigquery


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

    td_sql = Path(args.script_path).read_text()
    td_sql = td_sql.replace("\n", "")

    if args.sql_style == "bigquery":
        converted_sql = bigquery.select_converter(txt)
    else:
        print("Only Bigquery is yet supported")

    # this overwrites. fix that
    Path(args.script_path).write_text(converted_sql)


if __name__ == "__main__":
    main()
