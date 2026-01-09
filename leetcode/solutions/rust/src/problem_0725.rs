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
    pub fn split_list_to_parts(head: Option<Box<ListNode>>, k: i32) -> Vec<Option<Box<ListNode>>> {
        let mut parts = Vec::<Option<Box<ListNode>>>::new();
        let mut list_repr = Vec::<i32>::new();

        let mut current: Option<Box<ListNode>> = head;

        while let Some(ref mut node) = current {
            list_repr.push(node.val);
            current = node.next.take();
        }

        let num_nodes = list_repr.len();
        let mut num_elem_per_part = vec![num_nodes as i32 / k; k as usize];

        for idx in 0..num_nodes % k as usize {
            num_elem_per_part[idx] += 1;
        }

        let mut list_repr_cursor: usize = 0;

        for num_elem in num_elem_per_part {
            if num_elem == 0 {
                parts.push(None);
                continue;
            }

            let mut dummy = ListNode::new(0);
            let mut current = &mut dummy;

            for _ in 0..num_elem {
                current.next = Some(Box::new(ListNode::new(list_repr[list_repr_cursor])));
                current = current.next.as_mut().unwrap();
                list_repr_cursor += 1;
            }

            parts.push(dummy.next);
        }

        return parts;
    }
}

pub fn run_tests() {}
