#include "lists.h"

/**
 * check_cycle - Check if a cycle exist in a linked list
 * @list: Single linked list to check for cycles
 * Return: 0 if no cycle, 1 if a cycle is found
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	if (list)
	{
		do {
			first = first->next;
			second = second->next->next;

			if (first == second)
				return (1);

		} while (first->next && second->next->next);
	}
	return (0);
}
