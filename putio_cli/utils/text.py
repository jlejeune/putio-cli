def add_title_to_table(table, title):
    """
    Configure title of a table

    :rtype: str
    :type table: PrettyTable
    :type title: str
    """
    length = len(table.get_string().split('\n')[0])
    retval = '+' + ''.center(length - 2, '-') + '+\n'
    retval += '|' + title.center(length - 2) + '|\n'
    retval += table.get_string()
    return retval
