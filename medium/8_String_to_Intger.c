int myAtoi(char* s) {
    long	res;
	long	sign;
	int		i;

	res = 0;
	sign = 1;
	i = 0;
	while ((s[i] >= 9 && s[i] <= 13) || s[i] == 32)
		i++;
	if (s[i] == '-' || s[i] == '+')
		if (s[i++] == '-')
			sign = -1;
	while (s[i] >= '0' && s[i] <= '9')
	{
		res = res * 10 + (s[i++] - '0');
		if (res * sign > 2147483647)
			return (2147483647);
		if (res * sign < (-2147483648))
			return (-2147483648);
	}
	return (res * sign);

}
