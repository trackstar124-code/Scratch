# HW_01.py

# import library
import csv

# PROBLEM 1
def load_pixar_data(filename):
    """
    Loads Pixar films data from a CSV file.

    Args:
    filename (str): Path to the CSV file containing Pixar films data.

    Returns:
    data (list): List of dictionaries with film data.
    """
    with open(filename, "r") as f:
        data = []
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def clean_pixar_data(data):
    """
    Cleans Pixar films data from a CSV file. 
    Removes rows with empty string value in 'film'.
    Converts numeric fields ('run_time', 'rotten_tomatoes', 'metacritic') to float if they are not empty strings.
    
    Args:
    data (list): list of dictionaries 
    
    Returns:
    tuple: a tuple containing:
        - clean_data_list (list): List of dictionaries with cleaned film data.
        - original_count (int): Integer of original number of rows in the CSV file.
        - removed_count (int): Integer of number of rows removed due to missing data.
        - final_count (int): Integer of final number of rows after cleaning.
    """
    original_count = len(data)
    clean_data_list = []

    for row in data:
        if (row['film'] is None or row['film'] == ''):
            continue
        for field in ('run_time', 'rotten_tomatoes', 'metacritic'):
            if (row[field] is None or row[field] == ''):
                row[field] = None
            else:
                row[field] = float(row[field])
        clean_data_list.append(row)

    final_count = len(clean_data_list)
    removed_count = original_count - final_count
    return clean_data_list, original_count, removed_count, final_count

# PROBLEM 2
def calculate_rt_score_statistics(data):
    """
    Analyzes Pixar films data to calculate Rotten Tomatoes scores statistics.
    Cannot use sort(), min(), max(), mean(), or sum() functions.
    Can use round() function to round the average score to 1 decimal place.

    Args:
    data (list): List of dictionaries containing cleaned Pixar films data.
    
    Returns:
    dictionary: A dictionary containing the following keys and values:
        - min_score (float): Minimum Rotten Tomatoes score.
        - max_score (float): Maximum Rotten Tomatoes score.
        - avg_score (float): Average Rotten Tomatoes score rounded to 1 decimal place.
    """
    min_score = None
    max_score = None
    count = 0
    total = 0
    for row in data:
        score = row['rotten_tomatoes']
        if (score is not None and score != ''):
            if min_score is None or score < min_score: min_score = score
            if max_score is None or score > max_score: max_score = score
            total += score
            count += 1
    avg_score = round(total / count, 1)
    return {'min_score': min_score, 'max_score': max_score, 'avg_score': avg_score}


# PROBLEM 3
# SETUP
num2month = {
    '01' : 'January',
    '02' : 'February',
    '03' : 'March',
    '04' : 'April',
    '05' : 'May',
    '06' : 'June',
    '07' : 'July',
    '08' : 'August',
    '09' : 'September',
    '10' : 'October',
    '11' : 'November',
    '12' : 'December'
}
# END SETUP

def get_most_popular_release_month(data):
    """
    Returns the most popular release month and the number of films released in that month.
    max() or sort() functions cannot be used.

    Args:
    data (list): List of dictionaries containing cleaned Pixar films data.

    Returns:
    tuple: A tuple containing:
        - most_popular_month (str): The month with the highest number of films released. 
                                    The month is represented as a string (e.g., "January").
        - total_films (int): The total number of films released in that month.
    """
    month_counts = {}
    best_month = None
    best_count = 0
    for row in data:
        date = row['release_date']
        if '-' in date:
            month = date.split('-')[1]   # YYYY-MM-DD
        else:
            month = date.split('/')[0]   # M/D/YYYY
        month_digits = month.zfill(2)
        month_name = num2month[month_digits]
        if month_name in month_counts:
            month_counts[month_name] += 1
        else:
            month_counts[month_name] = 1
    for month, count in month_counts.items():
        if count > best_count:
            best_month = month
            best_count = count
    return best_month, best_count

# PROBLEM 4(a)
def get_longest_and_shortest_films(data):
    """
    Analyzes Pixar films data to find the longest and shortest films.
    max(), min(), and sort() functions cannot be used.

    Args:
    data (list): List of dictionaries containing Pixar films data.

    Returns:
    dictionary: A dictionary with the following keys and values:
        - shortest_film (str): The title of the shortest film.
        - longest_film (str): The title of the longest film.
    """
    shortest_film = None
    longest_film = None
    shortest_time = None
    longest_time = None
    for row in data:
        run_time = row['run_time']
        if (run_time is not None and run_time != ''):
            if shortest_time is None or run_time < shortest_time:
                shortest_time = run_time
                shortest_film = row['film']
            if longest_time is None or run_time > longest_time:
                longest_time = run_time
                longest_film = row['film']
    return {'shortest_film': shortest_film, 'longest_film': longest_film}

# PROBLEM 4(b)
def get_runtime_category_counts(data):
    """
    Analyzes Pixar films data to categorize runtimes and count occurrences.

    Args:
    data (list): List of dictionaries containing Pixar films data.

    Returns:
    dictionary: A dictionary with runtime categories as keys and their counts as values.
        - 'short': Count of films with runtime < 90 minutes
        - 'medium': Count of films with runtime between 90 and 110 minutes (inclusive)
        - 'long': Count of films with runtime > 110 minutes
    """
    counts = {'short': 0, 'medium': 0, 'long': 0}
    for row in data:
        run_time = row['run_time']
        if (run_time is None or run_time == ''):
            continue
        if run_time < 90:
            counts['short'] += 1
        elif run_time <= 110:
            counts['medium'] += 1
        else:
            counts['long'] += 1
    return counts

# PROBLEM 4(c)
def get_runtime_by_rating(data, rating):
    """
    Returns the average runtime of films with a specific rating (e.g., 'G', 'PG', 'PG-13', 'R').
    Returns None if the rating is not valid or if there are no films with that rating.
    Can use round() function to round the average score to 1 decimal place.
    
    Args:
    data (list): List of dictionaries containing Pixar films data.
    rating (str): The film rating to filter by (options can be: 'G', 'PG', 'PG-13', 'R').

    Returns:
    float: The average runtime of films with the specified rating. Rounded to 1 decimal place.
    """
    if rating not in ('G', 'PG', 'PG-13', 'R'):
        return None
    total = 0
    count = 0
    for row in data:
        if row['film_rating'] == rating and (row['run_time'] is not None and row['run_time'] != ''):
            total += row['run_time']
            count += 1
    if count == 0:
        return None
    return round(total / count, 1)

# PROBLEM 5(a)
def remove_punctuation_and_articles(title):
    """
    Lowercases a film title, removes punctuation, and drops a leading article
    ('a', 'an', 'the') so titles can be compared (e.g. "The Incredibles" -> "incredibles").

    Args:
    title (str): The film title.

    Returns:
    str: The normalized title.
    """
    cleaned = ''
    for char in title.lower():
        if char.isalnum() or char == ' ':
            cleaned += char
    words = cleaned.split()
    if words and words[0] in ('a', 'an', 'the'):
        words = words[1:]
    return ' '.join(words)

def get_films_by_type(data, type_filter):
    """
    Filters the Pixar films data to get a list films by type (either 'original' or 'sequel').
    Sequels are films that are not original and can be the second or later in a series.
    Use remove_punctuation_and_articles function implemented above as a helper function.

    Args:
    data (list): List of dictionaries containing Pixar films data.
    type_filter (str): The type of film to filter by ('original' or 'sequel').

    Returns:
    list: A list of dictionaries containing only original films.
    """
    originals = []
    sequels = []
    seen_first_words = []
    for row in data:
        words = remove_punctuation_and_articles(row['film']).split()
        first_word = words[0] if words else ''
        # a film is a sequel if an earlier film starts with the same word
        if first_word in seen_first_words:
            sequels.append(row)
        else:
            originals.append(row)
            seen_first_words.append(first_word)
    if type_filter == 'original':
        return originals
    if type_filter == 'sequel':
        return sequels
    return []

# PROBLEM 5(b)
def calculate_originals_and_sequels_rt_scores(data):
    """
    Calculate the originals and sequals average Rotten Tomatoes scores.
    Uses the get_films_by_type functions to filter the data.
    Use lambda fucntion which uses sum() to calculate the average RT score.
    Can use round() function to round the average score to 1 decimal place.

    Args:
    data (list): List of dictionaries containing Pixar films data.

    Returns:
    dictionary: A dictionary with the following keys and values:
        - original_avg_rt_score (float): Average Rotten Tomatoes score for original films. Rounded to 1 decimal place.
        - sequel_avg_rt_score (float): Average Rotten Tomatoes score for sequels. Rounded to 1 decimal place.
    """
    average = lambda scores: round(sum(scores) / len(scores), 1) if scores else None
    originals = get_films_by_type(data, 'original')
    sequels = get_films_by_type(data, 'sequel')
    original_scores = [row['rotten_tomatoes'] for row in originals if (row['rotten_tomatoes'] is not None and row['rotten_tomatoes'] != '')]
    sequel_scores = [row['rotten_tomatoes'] for row in sequels if (row['rotten_tomatoes'] is not None and row['rotten_tomatoes'] != '')]
    return {
        'original_avg_rt_score': average(original_scores),
        'sequel_avg_rt_score': average(sequel_scores),
    }

# PROBLEM 6
def filter_top_five_films(data):
    """
    Filter the top five films based on their composite scores.
    This function should use lambda function for calculating the composite score.
    Use map() and sorted() to help sort your data based on composite score.

    Args:
    data (list): List of dictionaries containing Pixar films data.

    Returns:
    list: A list of dictionaries containing the top five films with their composite scores.
          The list is sorted in descending order by composite score. The dictionary contains:
            - 'film': The title of the film.
            - 'composite_score': The composite score of the film.
    """
    scored_films = [row for row in data
                    if (row['rotten_tomatoes'] is not None and row['rotten_tomatoes'] != '') and (row['metacritic'] is not None and row['metacritic'] != '')]
    # composite score = 40% Rotten Tomatoes + 60% Metacritic
    composite = lambda row: {
        'film': row['film'],
        'composite_score': round(0.4 * row['rotten_tomatoes'] + 0.6 * row['metacritic'], 1),
    }
    with_scores = map(composite, scored_films)
    ranked = sorted(with_scores, key=lambda item: item['composite_score'], reverse=True)
    return ranked[:5]


if __name__ == "__main__":
    print("HW 01: PIXAR FILMS DATA ANALYSIS")

    # Use this main function to call your functions and test them.

    # PROBLEM 1 - calling
    data = load_pixar_data('pixar_films.csv')
    print(data)
    data, original_count, removed_count, final_count = clean_pixar_data(data)
    print(data)
    
    # PROBLEM 2 - calling
    print("\nProblem 2")
    print(calculate_rt_score_statistics(data))

    # Problem 3 - calling
    print("\nProblem 3")
    print(get_most_popular_release_month(data))

    # Problem 4 - calling
    print("\nProblem 4")
    print(get_longest_and_shortest_films(data))
    print(get_runtime_category_counts(data))
    print(get_runtime_by_rating(data, 'G'))
    print(get_runtime_by_rating(data, 'PG'))
    print(get_runtime_by_rating(data, 'R'))

    # Problem 5 - calling
    print("\nProblem 5")
    print([row['film'] for row in get_films_by_type(data, 'original')])
    print([row['film'] for row in get_films_by_type(data, 'sequel')])
    print(calculate_originals_and_sequels_rt_scores(data))

    # PROBLEM 6 - calling
    print("\nProblem 6")
    print(filter_top_five_films(data))
