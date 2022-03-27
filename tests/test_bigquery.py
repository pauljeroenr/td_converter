import pytest
import src.bigquery as bigquery


def test_select_converter():
    td_sql = "sel a, median(b), median(ce) from schema.table group by a"
    bq_sql = "select a, percentile_cont(b, 0.5) over(), percentile_cont(ce, 0.5) over() from schema.table group by a"

    res = bigquery.select_converter(td_sql)
    assert res == bq_sql


def test_type_converter():
    td_sql = "create table schema.table (ae varchar(12), be char(8), ce smallint, de integer, ef float)"
    bq_sql = "create table schema.table (ae string, be string, ce int64, de int64, ef float64)"

    res = bigquery.type_converter(td_sql)
    assert res == bq_sql


def test_comparison_converter():
    td_sql = (
        "select a from schema.table where a eq 1 and b eq 1 and c ge 2 and de ne 45"
    )
    bq_sql = "select a from schema.table where a = 1 and b = 1 and c >= 2 and de != 45"

    res = bigquery.comparison_converter(td_sql)
    assert res == bq_sql
