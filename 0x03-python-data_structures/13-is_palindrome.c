#include "lists.h"
/**
 * recurPalindrome - this function checks if singly linked list is palindrome
 * @left: a pointer to head of singly linked list
 * @right: the head of singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int recurPalindrome(listint_t **left, listint_t *right)
{
	int a;

	if (right == NULL)
		return (1);

	a = recurPalindrome(left, right->next);
	if (a == 0)
		return (0);

	a = (right->n == (*left)->n);

	*left = (*left)->next;

	return (a);
}
/**
 * is_palindrome - this checks if singly linked list is palindrome
 * @head: a pointer to head of singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (!head)
		return (0);
	return (recurPalindrome(head, *head));
}
