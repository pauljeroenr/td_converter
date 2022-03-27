CREATE TABLE schema.table (
    test1 VARCHAR(255),
    test2 INTEGER,
    test3 CHAR(2)
);

SELECT
    test1,
    test3,
    MEDIAN(test2),
    MEDIAN(test3)
FROM
    schema.TABLE
WHERE
    test2 EQ 2
    AND test2 NE 0
