package solutions

import (
	"fmt"
	"strings"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func createLinkedList(vals []int) *ListNode {
	if len(vals) == 0 {
		return nil
	}
	head := &ListNode{Val: vals[0]}
	current := head
	for i := 1; i < len(vals); i++ {
		current.Next = &ListNode{Val: vals[i]}
		current = current.Next
	}
	return head
}

func isEqualLinkedList(l1, l2 *ListNode) bool {
	for l1 != nil && l2 != nil {
		if l1.Val != l2.Val {
			return false
		}
		l1 = l1.Next
		l2 = l2.Next
	}
	return l1 == nil && l2 == nil
}

func (l *ListNode) String() string {
	if l == nil {
		return "<nil>"
	}

	var sb strings.Builder
	sb.WriteString("[")

	current := l
	first := true
	count := 0
	limit := 50

	for current != nil {
		if !first {
			sb.WriteString(" -> ")
		}
		sb.WriteString(fmt.Sprintf("%d", current.Val))

		first = false
		current = current.Next

		count++
		if count >= limit {
			sb.WriteString(" -> ... (limit reached)")
			break
		}
	}
	sb.WriteString("]")

	return sb.String()
}
