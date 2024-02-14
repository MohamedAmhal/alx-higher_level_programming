-- this command is use to calaculate the average of the rows.
SELECT city, AVG(temperature) AS avg_temp FROM dump
GROUP BY city
ORDER BY avg_temp DESC;
