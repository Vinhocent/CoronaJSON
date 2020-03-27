# Corona JSON

the goal of this project is to provide coronavirus statistics in a .json format.

source of scrape: https://www.worldometers.info/coronavirus/#countries

## progress
Pretty much done.

I need to package and distribute this into a library now.

Other than that, you can clone this repo and include corona.py in your project.
You can either output the whole json by simply running `./corona.py`, or you 
can call it in your code like so:

    import corona
    var = corona.dump_json()
    usa_cases = var['USA']['total_cases']

    print(usa_cases)
    # 46,145

Felt kind of grim making this, but oh well. It works pretty good and I learned
some stuff.
