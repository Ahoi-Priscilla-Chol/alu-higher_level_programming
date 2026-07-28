-- lists score and name from second_table, excluding rows with no name, ordered by score descending
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
