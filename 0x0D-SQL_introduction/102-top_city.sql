-- this is a programm that display the average of the temperature in the months 7 and 8.
SELECT city, AVG(value) as avg_temp FROM temperatures
WHERE month = 7 or month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
