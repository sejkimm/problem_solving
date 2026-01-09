package solutions

import (
	"testing"
)

func TestProblem0206(t *testing.T) {
	t.Run("Example 1", func(t *testing.T) {
		input := createLinkedList([]int{1, 2, 3, 4, 5})
		expected := createLinkedList([]int{5, 4, 3, 2, 1})

		result := reverseList(input)

		if !isEqualLinkedList(expected, result) {
			t.Errorf("Expected %s, but got %s", expected, result)
		}
	})

	t.Run("Example 2", func(t *testing.T) {
		input := createLinkedList([]int{1, 2})
		expected := createLinkedList([]int{2, 1})

		result := reverseList(input)

		if !isEqualLinkedList(expected, result) {
			t.Errorf("Expected %s, but got %s", expected, result)
		}
	})

	t.Run("Example 3", func(t *testing.T) {
		input := createLinkedList([]int{})
		expected := createLinkedList([]int{})

		result := reverseList(input)

		if !isEqualLinkedList(expected, result) {
			t.Errorf("Expected %s, but got %s", expected, result)
		}
	})
}
