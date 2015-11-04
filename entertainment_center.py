__author__ = 'abhig'

import media
import fresh_tomatoes
import stories
import url_links

"""Created instances for each movie"""

toy_story = media.Movie("Toy Story",
                        stories.toy_story_stry,
                        url_links.toy_story_pos,
                        url_links.toy_story_trailer)
the_dark_knight = media.Movie("The Dark Knight",
                              stories.the_dark_knight_stry,
                              url_links.the_dark_knight_pos,
                              url_links.the_dark_knight_trailer)
avatar = media.Movie("Avatar",
                     stories.avatar_stry,
                     url_links.avatar_pos,
                     url_links.avatar_trailer)
spectre = media.Movie("Spectre",
                      stories.spectre_stry,
                      url_links.spectre_pos,
                      url_links.spectre_trailer)
argo = media.Movie("Argo",
                   stories.argo_stry,
                   url_links.argo_pos,
                   url_links.argo_trailer)
the_intern = media.Movie("The Intern",
                         stories.the_intern_stry,
                         url_links.the_intern_pos,
                         url_links.the_intern_trailer)

# created the movie list and called open_movies_page

movie_list = [avatar, toy_story, the_dark_knight, argo, spectre, the_intern]
fresh_tomatoes.open_movies_page(movie_list)
