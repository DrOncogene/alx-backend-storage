-- ranks the metal bands origin by number of fans
SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY SUM(fans) DESC;
