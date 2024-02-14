-- this programm is also the same of the last one.
SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state
ORDER BY state;
