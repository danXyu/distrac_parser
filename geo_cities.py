import re;

## Function: getCities(), allows the caller to retrieve a copy (in javascript array format) of
 # the cities in the preloaded seed file.
 ##
def getCities():

    # Open the cities5000.txt file, for parsing.
    f = open('cities5000.txt', 'r');

    # Create posts array to later stringify.
    posts = [];

    # Iterate over each line in the file and create a post from it.
    for line in f:

        # Split lines by delimiter: '\t'
        case = re.split('\t', line);
        posts.append({
            "geonameid":          case[0],
            "name":               case[1],
            "asciiname":          case[2],
            "alternatenames":     case[3],
            "location":           {
                "type": "Point",
                "coordinates": [float(case[5]), float(case[4])]
            },
            "featureclass":       case[6],
            "featurecode":        case[7],
            "countrycode":        case[8],
            "cc2":                case[9],
            "population":         case[14],
            "elevation":          case[15],
            "dem":                case[16],
            "timezone":           case[17],
            "modificationdate":   case[18]
        });

    # Return the posts array. Hopefully this works.
    return posts