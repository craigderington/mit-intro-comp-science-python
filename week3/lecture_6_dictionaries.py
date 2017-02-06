#! /usr/bin/python

eminem_song = ['Look,', 'I', 'was', 'gonna', 'go', 'easy', 'on', 'you', 'and', 'not', 'to', 'hurt', 'your', 'feelings', 'But', 'I', 'am', 'only', 'going', 'to', 'get', 'this', 'one', 'chance', 'Somethings', 'wrong,', 'I', 'can', 'feel', 'it', 'Six', 'minutes,', 'Slim', 'Shady,', 'you', 'are', 'on', 'Just', 'a', 'feeling', 'I', 'have', 'got,', 'like', 'somethings', 'about', 'to', 'happen,', 'but', 'I', 'do', 'not', 'know', 'what', 'If', 'that', 'means,', 'what', 'I', 'think', 'it', 'means,', 'we', 'are', 'in', 'trouble,', 'big', 'trouble,', 'And', 'if', 'he', 'is', 'as', 'bananas', 'as', 'you', 'say,', 'I', 'am', 'not', 'taking', 'any', 'chances', 'You', 'were', 'just', 'what', 'the', 'doctor', 'ordered.']


def lyrics_to_freqs(lyrics):
    my_dict = {}
    for word in lyrics:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1

    return my_dict


def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)

    return (words, best)


def words_often(freqs, min_times):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= min_times:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True

    return result


print(words_often(lyrics_to_freqs(eminem_song), 5))

my_lyrics = most_common_words(lyrics_to_freqs(eminem_song))
print(my_lyrics)


