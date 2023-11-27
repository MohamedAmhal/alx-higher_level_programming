#include "lists.h"


int check_cycle(listint_t *list)
{
	listint_t *a = list, *b = list;

	while (b && b->next)
	{
		a = a->next;
		b = b->next->next;
		if (a == b)
			return (1);
	}
	return (0);
}
