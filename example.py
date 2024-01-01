from main import Similarity

c = Similarity()
c.add_strings("something apurva apratim",
                "something apratim apurva",
                "please this would be of great help if you could help me in creating a draft which would not be something viable",
                "please what is this! great help if you could help me in creating a draft which would not be something viable",
                "something",
                "something",
                "there sometimes wll be things that would nt be thereif",
                "nothing something there here",
                "there apurva nothing"
              )

c.generate()
for a in c.ratios:
    print(a)
