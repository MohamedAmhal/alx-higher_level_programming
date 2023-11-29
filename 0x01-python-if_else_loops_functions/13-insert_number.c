#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node _ insert the data on the linked liss
 * @head: this is the head
 * @number: this is the data
 * Return: 0 or 1
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!node || new->n < node->n)
	{
		new->next = node;
		return (*head = new);
	}

	while (node)
	{
		if (!node->next || new->n < node->next->n)
		{
			new->next = node->next;
			node->next = new;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}	
