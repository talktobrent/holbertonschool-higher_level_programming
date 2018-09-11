#include "lists.h"

/**
  * check_cycle - checks if linked list has a cycle
  * @list: head of lined list given
  * Return: 1 if cycle, 0 if not
  */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (list == NULL)
		return (0);

	while (fast->next != NULL)
	{
		fast = fast->next;
		if (fast->next != NULL)
			fast = fast->next;
		if (fast == slow)
			return (1);
		slow = slow->next;
	}

	return (0);
}
