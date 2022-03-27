import re
from typing import Dict


def select_converter(sql_string: str) -> str:
    functions_to_convert = {
        r"(^|\s)sel ": "select ",
        r"median\(.+?\)": "percentile_cont(placeholder, 0.5) over()",
    }

    return _replace_matches(functions_to_convert, sql_string)


def type_converter(sql_string: str) -> str:
    types_to_convert = {
        r"(\s)character\(.+?\)": " string",
        r"(\s)varchar\(.+?\)": " string",
        r"(\s)char\(.+?\)": " string",
        r"(\s)integer": " int64",
        r"(\s)smallint": " int64",
        r"(\s)byteint": " int64",
        r"(\s)bigint": " int64",
        r"(\s)float": " float64",
    }

    return _replace_matches(types_to_convert, sql_string)


def comparison_converter(sql_string: str) -> str:
    comparison_operator_to_convert = {
        r"(\s)eq(\s)": " = ",
        r"(\s)le(\s)": " <= ",
        r"(\s)lt(\s)": " < ",
        r"(\s)ne(\s)": " != ",
        r"(\s)ge(\s)": " >= ",
        r"(\s)gt(\s)": " > ",
    }

    return _replace_matches(comparison_operator_to_convert, sql_string)


def schema_converter(sql_string: str) -> str:
    schema_to_convert = {}

    return _replace_matches(schema_to_convert, sql_string)


def _replace_matches(patterns: Dict, sql: str) -> str:
    for key, value in patterns.items():
        regex = re.compile(key)
        if regex.search(sql):
            matches = regex.findall(sql)
            for match in matches:
                if re.search("placeholder", value):
                    colname = re.findall(r"\((.+?)\)", match)
                    temp_value = re.sub("placeholder", colname[0], value)
                else:
                    temp_value = value
                sql = regex.sub(temp_value, sql, 1)

    return sql
