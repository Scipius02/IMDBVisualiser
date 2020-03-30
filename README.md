# IMDBVisualiser
Simple script that webscrapes for a tv show then displays the average user scores for all episodes in a plot

# to_do: 
      fix the matplotlib representation - currently the y axis is broken
      split IMDBScrapy into its own class
      import into the IMDBVisualiser script to make modular
      add in line entry "TV Show" functionality - this should be easy, especially if you pair it with the OMDB API to grab the show id#. however, the point of doing this is to not be reliant on API's since that's cheating.
      not sure if there's a way around all of the get requests - the html for imdb is a little convoluted, with usable data hidden across a bunch of pages, hence all the loading and the tremendous run time

# Acknowledgements
inspired by u/BoMcCready https://www.reddit.com/r/dataisbeautiful/comments/brnktf/tv_show_imdb_user_rating_trajectories_oc/
  his implementation is in tableau, took the idea and ran with it to create a python version to teach myself webscraping
