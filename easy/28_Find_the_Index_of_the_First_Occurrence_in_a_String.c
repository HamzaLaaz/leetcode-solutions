int ft_strlen(char *str){
    int i = 0;
    while (str[i])
        i++;
    return i;
}
int strStr(char *haystack, char *needle) {
    int j = 0;
    int lh = ft_strlen(haystack);
    int ln = ft_strlen(needle);

    if (ln <= lh) {
        while (j < lh) {
            int i = 0;
            if (haystack[j] == needle[i]) {
                int k = j;
                while (i < ln) {
                    if (haystack[k] == needle[i]) {
                        i++;
                        if (k < lh - 1) {
                            k++;
                        }
                    } else {
                        break;
                    }
                }
                if (i == ln) {
                    return j;
                }
            }
            j++;
        }
    }
    return -1;
}
