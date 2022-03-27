import argparse
from pathlib import Path
import bigquery
import re


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
        default="bigquery",
        help="where to run the sql script",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    td_sql = Path(args.script_path).read_text()
    td_sql = td_sql.lower()

    if args.sql_style == "bigquery":
        temp_sql = td_sql
        temp_sql = bigquery.select_converter(temp_sql)
        temp_sql = bigquery.type_converter(temp_sql)
        temp_sql = bigquery.comparison_converter(temp_sql)
    else:
        print("#######################################################################")
        print("Only Bigquery is yet supported")
        print("#######################################################################")
        return

    new_file = re.sub(r"[^\/]+$", "converted.sql", args.script_path)
    Path(new_file).write_text(temp_sql)

    print("###########################################################################")
    print("The following parts wont be changed yet")
    print("1) Alias of subqueries can not be used")
    print("1) Use CTE instead of subqueries")
    print("2) select TOP does not work in bigquery")
    print("2) use LIMIT at the end of the query")
    print("3) qualify can not be used in bigquery")
    print("3) use ROWNUMBER with PARTITION BY instead")
    print("###########################################################################")

    return


if __name__ == "__main__":
    main()
