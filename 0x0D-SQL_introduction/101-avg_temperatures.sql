-- this command is use to calaculate the average of the rows.
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
