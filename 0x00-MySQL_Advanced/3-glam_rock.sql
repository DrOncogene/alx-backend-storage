-- ranks Glam rock style bands by their longevity
SELECT band_name, (split - formed) as lifespan
FROM metal_bands
WHERE style='Glam rock'
ORDER BY lifespan DESC;
