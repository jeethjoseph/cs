# Problem Set 4A
# Name: Jeeth Joseph
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return sequence
    else:
        first_character = sequence[0]
        rest_of_the_characters = sequence[1:]
        permutations_of_rest = get_permutations(rest_of_the_characters)
        return_list = []
        for element in permutations_of_rest:
            for position  in range (len(element) + 1):
                element_after_insertion = ''
                if position == 0:
                    element_after_insertion = first_character + element
                elif position == (len(element)): #Inserting at the end where index is out of bounds
                    element_after_insertion = element + first_character
                else:
                    element_after_insertion = element[0:position]+first_character+element[position:len(element)]
                return_list.append(element_after_insertion)
        return return_list


if __name__ == '__main__':
    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'dcode'
    print('Input:', example_input)
    print('Expected Output:', ['dcode','dcoed','dcdoe','dcdeo','dceod','dcedo','doced','docde','dodec','dodce','doedc','doecd','ddcoe','ddceo','ddoce','ddoec','ddeco','ddeoc','decdo','decod','deodc','deocd','dedoc','dedco','cdeod','cdedo','cdoed','cdode','cddeo','cddoe','coedd','coedd','codde','coded','codde','coded','cdedo','cdeod','cddeo','cddoe','cdoed','cdode','cedod','ceddo','cedod','ceddo','ceodd','ceodd','oddec','oddce','odedc','odecd','odcde','odced','ocdde','ocded','ocedd','ocedd','ocded','ocdde','odced','odcde','odecd','odedc','oddce','oddec','oecdd','oecdd','oeddc','oedcd','oeddc','oedcd','ddcoe','ddceo','ddoce','ddoec','ddeco','ddeoc','dcdeo','dcdoe','dcoed','dcode','dceod','dcedo','dodce','dodec','docde','doced','doedc','doecd','dedoc','dedco','decod','decdo','deocd','deodc','eddco','eddoc','edcdo','edcod','edodc','edocd','ecdod','ecddo','ecdod','ecddo','ecodd','ecodd','eoddc','eodcd','eoddc','eodcd','eocdd','eocdd','edocd','edodc','eddco','eddoc','edcdo','edcod'])
    print('Actual Output:', get_permutations(example_input))

    import collections
    compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
    test_permutations = ['dcode','dcoed','dcdoe','dcdeo','dceod','dcedo','doced','docde','dodec','dodce','doedc','doecd','ddcoe','ddceo','ddoce','ddoec','ddeco','ddeoc','decdo','decod','deodc','deocd','dedoc','dedco','cdeod','cdedo','cdoed','cdode','cddeo','cddoe','coedd','coedd','codde','coded','codde','coded','cdedo','cdeod','cddeo','cddoe','cdoed','cdode','cedod','ceddo','cedod','ceddo','ceodd','ceodd','oddec','oddce','odedc','odecd','odcde','odced','ocdde','ocded','ocedd','ocedd','ocded','ocdde','odced','odcde','odecd','odedc','oddce','oddec','oecdd','oecdd','oeddc','oedcd','oeddc','oedcd','ddcoe','ddceo','ddoce','ddoec','ddeco','ddeoc','dcdeo','dcdoe','dcoed','dcode','dceod','dcedo','dodce','dodec','docde','doced','doedc','doecd','dedoc','dedco','decod','decdo','deocd','deodc','eddco','eddoc','edcdo','edcod','edodc','edocd','ecdod','ecddo','ecdod','ecddo','ecodd','ecodd','eoddc','eodcd','eoddc','eodcd','eocdd','eocdd','edocd','edodc','eddco','eddoc','edcdo','edcod']
    print("Comparing online permutation to local: ", compare(test_permutations,get_permutations('dcode')))
    # Put three example test cases here (for your sanity, limit your inputs
    # to be three characters or fewer as you will have n! permutations for a
    # sequence of length n)

    pass #delete this line and replace with your code here

