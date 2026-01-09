struct Solution;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn postorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut route: Vec<i32> = Vec::new();

        fn traverse(node: Option<Rc<RefCell<TreeNode>>>, route: &mut Vec<i32>) {
            if let Some(current_node) = node {
                let current_node = current_node.borrow();

                traverse(current_node.left.clone(), route);
                traverse(current_node.right.clone(), route);
                route.push(current_node.val);
            }
        }

        traverse(root, &mut route);
        return route;
    }
}

pub fn run_tests() {}
