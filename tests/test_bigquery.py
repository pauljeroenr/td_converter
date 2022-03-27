import pytest
import src.bigquery as bigquery


def test_select_converter():

    td_sql = "sel a, median(b), median(ce) from schema.table group by a"
    bq_sql = "select a, percentile_cont(b, 0.5) over(), percentile_cont(ce, 0.5) over() from schema.table group by a"

    res = bigquery.select_converter(td_sql)
    assert res == bq_sql
