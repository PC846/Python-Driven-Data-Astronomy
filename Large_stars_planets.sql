/*Week 3: Simple querying*/

SELECT radius, t_eff FROM Star
WHERE radius > 1;

SELECT kepler_id, t_eff FROM Star
WHERE t_eff BETWEEN 5000 AND 6000; 

SELECT kepler_name, radius FROM Planet
WHERE kepler_name IS NOT NULL AND radius BETWEEN 1 AND 3;

SELECT MIN(radius), MAX(radius), AVG(radius), STDDEV(radius) FROM Planet
WHERE kepler_name IS NULL;

SELECT kepler_id, COUNT(koi_name) from Planet
GROUP BY kepler_id 
HAVING COUNT(koi_name) > 1
ORDER BY COUNT(koi_name) DESC;