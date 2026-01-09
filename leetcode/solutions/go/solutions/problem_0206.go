package solutions

func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	var previous *ListNode
	current := head

	for current != nil {
		next := current.Next
		current.Next = previous
		previous = current
		current = next
	}

	return previous
}
