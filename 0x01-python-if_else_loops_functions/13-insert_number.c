#include "lists.h"

/**
 * insert_node - inserts new node into sorted linked list
 * @head: head of linked list
 * @number: n value of new node
 * Description: inserts new node into correct place in linked list
 * according to value of n
 * Return: pointer to new node, NULL if fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *runner, *newnode;

	if (head == NULL)
		return (NULL);

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);

	newnode->n = number;

	if (*head == NULL)
	{
		*head = newnode;
		newnode->next = NULL;
		return (newnode);
	}

	runner = *head;
	if (runner->n >= number)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}

	while (runner->next != NULL)
	{
		if (runner->next->n >= number)
			break;
		runner = runner->next;
	}

	newnode->next = runner->next;
	runner->next = newnode;

	return (newnode);
}
