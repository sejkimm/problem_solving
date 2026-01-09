struct Solution;

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
    pub fn gcd(a: i32, b: i32) -> i32 {
        if b == 0 {
            return a.abs();
        } else {
            return Self::gcd(b, a % b);
        }
    }

    pub fn insert_greatest_common_divisors(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy = ListNode::new(0);
        let mut current = head;
        let mut tail = &mut dummy;

        // Needs optimization
        while let Some(ref mut node) = current {
            let temp_next_node = node.next.take();

            if let Some(ref next_node) = temp_next_node {
                let mut new_node = ListNode::new(Self::gcd(node.val, next_node.val));
                new_node.next = Some(next_node.clone());

                tail.next = Some(node.clone());
                tail = tail.next.as_mut().unwrap();
                tail.next = Some(Box::new(new_node));
                tail = tail.next.as_mut().unwrap();
            } else {
                tail.next = Some(Box::new(ListNode::new(node.val)));
                break;
            }

            current = temp_next_node;
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
        create_linked_list(vec![18, 6, 6, 2, 10, 1, 3]),
        Solution::insert_greatest_common_divisors(create_linked_list(vec![18, 6, 10, 3]))
    );
    assert_eq!(
        create_linked_list(vec![7]),
        Solution::insert_greatest_common_divisors(create_linked_list(vec![7]))
    );
}
