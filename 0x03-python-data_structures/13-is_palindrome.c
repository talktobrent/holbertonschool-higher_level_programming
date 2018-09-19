#include "lists.h"

/**
 * is_palindrome - finds if linked list is palindrome
 * @head: head of linked list
 * Description: checks all 'n' values in singly linked list to
 * see if palindrome
 * Return: 0 if not pilindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *mover, *front, *back;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	mover = *head;
	front = *head;
	back = *head;

	while (back->next != NULL)
		back = back->next;

	while (front != back)
	{
		if (front->n != back->n)
			return (0);
		while (mover->next != back)
			mover = mover->next;
		if (mover != front)
			back = mover;
		front = front->next;
		mover = front;
	}
	return (1);
}

