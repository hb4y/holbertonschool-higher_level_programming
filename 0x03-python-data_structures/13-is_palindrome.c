#include "lists.h"
/**
  * is_palindrome - check if is palindrome
  * @head: head of list
  * Return: 0 if not pal 1 is pal
  */
int is_palindrome(listint_t **head)
{
	listint_t *h;
	int len, i;
	int aux[4096];

	if (!head || !(*head))
		return (1);
	h = *head;

	for (len = 0; h; h = h->next, len++)
		aux[len] = h->n;

	if (len == 1)
		return (1);

	for (i = 0; i < len; i++, len--)
	{
		if (aux[i] != aux[len - 1])
			return (0);
	}

	return (1);
}
