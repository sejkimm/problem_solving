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
    pub fn spiral_matrix(m: i32, n: i32, head: Option<Box<ListNode>>) -> Vec<Vec<i32>> {
        let mut matrix = vec![vec![-1; n as usize]; m as usize];
        let mut current = head;

        let mut boundary: (i32, i32) = (m - 1, n - 1);
        let mut current_iter: (i32, i32) = (0, 0);
        let mut cursor: (i32, i32) = (0, 0);
        let mut direction: (i32, i32) = (0, 1);

        while let Some(ref mut node) = current {
            matrix[cursor.0 as usize][cursor.1 as usize] = node.val;
            current = node.next.take();

            if direction == (0, 1) && current_iter.1 == boundary.1 {
                current_iter = (0, 0);
                boundary = (boundary.0 - 1, boundary.1);
                direction = (1, 0);
            } else if direction == (1, 0) && current_iter.0 == boundary.0 {
                current_iter = (0, 0);
                boundary = (boundary.0, boundary.1 - 1);
                direction = (0, -1);
            } else if direction == (0, -1) && current_iter.1 == boundary.1 {
                current_iter = (0, 0);
                boundary = (boundary.0 - 1, boundary.1);
                direction = (-1, 0);
            } else if direction == (-1, 0) && current_iter.0 == boundary.0 {
                current_iter = (0, 0);
                boundary = (boundary.0, boundary.1 - 1);
                direction = (0, 1);
            } else {
                current_iter = (
                    current_iter.0 + direction.0.abs(),
                    current_iter.1 + direction.1.abs(),
                );
            }
            cursor = (cursor.0 + direction.0, cursor.1 + direction.1);
        }

        return matrix;
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
        vec![
            vec![3, 0, 2, 6, 8],
            vec![5, 0, -1, -1, 1],
            vec![5, 2, 4, 9, 7]
        ],
        Solution::spiral_matrix(
            3,
            5,
            create_linked_list(vec![3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])
        )
    )
}
