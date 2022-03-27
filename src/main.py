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

    print(args.script_path)
    print(args.sql_style)

    td_sql = Path(args.script_path).read_text()
    td_sql = td_sql.lower()

    if args.sql_style == "bigquery":
        temp_sql = td_sql
        temp_sql = bigquery.select_converter(temp_sql)
        temp_sql = bigquery.type_converter(temp_sql)
        temp_sql = bigquery.comparison_converter(temp_sql)
    else:
        print("Only Bigquery is yet supported")

    new_file = re.sub(r"[^\/]+$", "converted.sql", args.script_path)
    Path(new_file).write_text(temp_sql)

    print("###########################################################################")
    print("Hinweis was noch geaendert werden muss")
    print("1) Alias von Subqueries koennen nicht in der Query benutzt werden")
    print("1) Statt Subquery besser als CTE-Konstrukt einbauen")
    print("2) Select Top funktioniert nicht in Bigquery")
    print("2) Stattdessen am Ende der Query ein LIMIT einbauen")
    print("3) Qualify kann nicht in Bigquery genutzt werden")
    print("3) Stattdessen mit Rownumber denselben Effekt erzielen")
    print("###########################################################################")


if __name__ == "__main__":
    main()
