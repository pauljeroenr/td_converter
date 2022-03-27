import re


def select_converter(sql_string: str) -> str:
    functions_to_convert = {
        r"(^|\s)sel ": "select ",
        r"median\(.+?\)": "percentile_cont(placeholder, 0.5) over()",
    }

    for key, value in functions_to_convert.items():
        regex = re.compile(key)
        if regex.search(sql_string):
            matches = regex.findall(sql_string)
            for match in matches:
                if re.search("placeholder", value):
                    colname = re.findall(r"\((.+?)\)", match)
                    temp_value = re.sub("placeholder", colname[0], value)
                else:
                    temp_value = value
                sql_string = regex.sub(temp_value, sql_string, 1)

    return sql_string
