#include "lists.h"
/**
 * get_nth - get the nth element of list
 * @head: head of list
 * @nth: nth pos
 * Return: value of n en nth pos
 */
int get_nth(listint_t **head, int nth)
{
	int i;
	listint_t *aux;

	aux = *head;
	for (i = 0; i < nth - 1; aux = aux->next, i++)
		;
	return (aux->n);
}
/**
  * is_palindrome - check if is palindrome
  * @head: head of list
  * Return: 0 if not pal 1 is pal
  */
int is_palindrome(listint_t **head)
{
	listint_t *h;
	int len, i;

	if (!head || !(*head))
		return (0);
	h = *head;

	for (len = 0; h; h = h->next, len++)
		;
	for (i = 1; i <= len; i++, len--)
	{
		if (get_nth(head, i) != get_nth(head, len))
			return (0);
	}

	return (1);
}
