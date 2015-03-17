import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life",
           "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
           "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Movie("Avatar"," A marine on an alien planet",
                     "https://www.google.com.gh/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0CAcQjRw&url=http%3A%2F%2Fsmellslikescreenspirit.com%2F2009%2F08%2Favatar-teaser-poster%2F&ei=D_4HVavjEYvoUu2Wg6AL&bvm=bv.88198703,d.d24&psig=AFQjCNEwiO52HDyWmjtc-e-hHZUq7sbcXg&ust=1426673546240702",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")
#print(avatar.storyline)
#avatar.show_trailer()
school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
            "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
            "https://ww.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
            "http://upload.wikimedia/en/5/50/RatatouillePoster.jpg",
            "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors",
            "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
            "https://www.youtube.com/watch?v=atLg2wQQdvU")

hunger_games = media.Movie("Hunger Games", "A really real reality show",
            "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
            "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
