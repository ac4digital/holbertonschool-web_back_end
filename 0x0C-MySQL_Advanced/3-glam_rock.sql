-- Lists all band with Glam as their main style, ranked by
-- their longetivity
SELECT band_name, IFNULL(split, 2022) - IFNULL(formed, 0) AS 'lifespan'
FROM metal_bands WHERE FIND_IN_SET('Glam rock', style) ORDER BY lifespan DESC;
