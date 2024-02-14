-- this command is to show how to group a colum with another column in the table.
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score;
