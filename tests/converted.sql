create table schema.table (
    test1 string,
    test2 int64,
    test3 string
);

select
    test1,
    test3,
    percentile_cont(test2, 0.5) over(),
    percentile_cont(test3, 0.5) over()
from
    schema.table
where
    test2 = 2
    and test2 != 0
