-- Lists all shows without a genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_matches
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_matches DESC;
