-- counting num of shows that has the same genre
SELECT tv_genres.title AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.title
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;