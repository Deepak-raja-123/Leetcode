#include <stdlib.h>
#include <string.h>

static int findWord(char **words, int wordsSize, char *word) {
    for (int i = 0; i < wordsSize; i++) {
        if (strcmp(words[i], word) == 0) {
            return i;
        }
    }

    return -1;
}

int* findSubstring(char* s, char** words, int wordsSize,
                   int* returnSize) {
    
    *returnSize = 0;

    int sLen = strlen(s);
    int wordLen = strlen(words[0]);
    int totalLen = wordLen * wordsSize;

    int *result = malloc(sLen * sizeof(int));

    if (totalLen > sLen) {
        return result;
    }

    /*
     * Count how many times each word appears in words.
     */
    int *required = calloc(wordsSize, sizeof(int));

    for (int i = 0; i < wordsSize; i++) {
        int index = findWord(words, wordsSize, words[i]);
        required[index]++;
    }

    /*
     * Try each possible alignment.
     */
    for (int offset = 0; offset < wordLen; offset++) {

        int left = offset;
        int right = offset;
        int count = 0;

        int *current = calloc(wordsSize, sizeof(int));

        while (right + wordLen <= sLen) {

            char word[31];

            memcpy(word, s + right, wordLen);
            word[wordLen] = '\0';

            right += wordLen;

            int index = findWord(words, wordsSize, word);

            /*
             * Word is not in the required list.
             */
            if (index == -1) {
                memset(current, 0, wordsSize * sizeof(int));
                count = 0;
                left = right;
                continue;
            }

            current[index]++;
            count++;

            /*
             * Too many copies of this word.
             * Move left until it becomes valid.
             */
            while (current[index] > required[index]) {

                char leftWord[31];

                memcpy(leftWord, s + left, wordLen);
                leftWord[wordLen] = '\0';

                int leftIndex =
                    findWord(words, wordsSize, leftWord);

                current[leftIndex]--;
                left += wordLen;
                count--;
            }

            /*
             * We have exactly wordsSize words.
             */
            if (count == wordsSize) {
                result[*returnSize] = left;
                (*returnSize)++;

                /*
                 * Move forward one word to search
                 * for the next possible answer.
                 */
                char leftWord[31];

                memcpy(leftWord, s + left, wordLen);
                leftWord[wordLen] = '\0';

                int leftIndex =
                    findWord(words, wordsSize, leftWord);

                current[leftIndex]--;
                left += wordLen;
                count--;
            }
        }

        free(current);
    }

    free(required);

    return result;
}