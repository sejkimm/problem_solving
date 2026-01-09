struct Solution;

//Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Solution {
    pub fn remove_elements(head: Option<Box<ListNode>>, val: i32) -> Option<Box<ListNode>> {
        let mut dummy = ListNode { val: 0, next: head };
        let mut current = &mut dummy;

        while let Some(ref mut node) = current.next {
            if node.val == val {
                current.next = node.next.take();
            } else {
                current = current.next.as_mut().unwrap();
            }
        }

        return dummy.next;
    }
}

fn create_linked_list(values: Vec<i32>) -> Option<Box<ListNode>> {
    let mut current = None;
    for &value in values.iter().rev() {
        let mut new_node = ListNode::new(value);
        new_node.next = current;
        current = Some(Box::new(new_node));
    }

    return current;
}

pub fn run_tests() {
    assert_eq!(
        create_linked_list(vec![1, 2, 3, 4, 5]),
        Solution::remove_elements(create_linked_list(vec![1, 2, 6, 3, 4, 5, 6]), 6)
    );
    assert_eq!(
        create_linked_list(vec![]),
        Solution::remove_elements(create_linked_list(vec![]), 1)
    );
    assert_eq!(
        create_linked_list(vec![]),
        Solution::remove_elements(create_linked_list(vec![7, 7, 7, 7]), 7)
    )
}
