DELETE FROM Person
WHERE id NOT IN (
    SELECT keeper_id FROM (
        SELECT MIN(id) AS keeper_id
        FROM Person
        GROUP BY email
    ) AS temp_table
);