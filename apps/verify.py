def has_relevant_context(distances, threshold=1.2):
    """
    Returns True if at least one retrieved document
    is close enough to the query.
    """

    if len(distances) == 0:
        return False

    best_distance = min(distances)

    return best_distance <= threshold