#include "lists.h"

/**
 * insert_node - Insert a new node in a linked list
 * @head: head of the list
 * @number: the number for the new node
 * Return: New node on sucess or NULL if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *tmp = *head;

	new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;

	if (!(*head))
	{
		new->next = NULL;
		*head = new;
		return (new);
	}

	if (tmp->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	for (; tmp; tmp = tmp->next)
	{
		if (!(tmp->next))
		{
			new->next = NULL;
			tmp->next = new;
			return (new);
		}
		if (tmp->next->n >= number)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
	}

	free(new);
	return (NULL);
}
