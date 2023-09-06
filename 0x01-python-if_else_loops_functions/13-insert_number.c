#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: pointer to the pointer of first node of the list
 * @number: new number to insert
 *
 * Return: address of the new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	current = *head;

	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	new->next = current->next;
	current->next = new;
	return (new);
}
