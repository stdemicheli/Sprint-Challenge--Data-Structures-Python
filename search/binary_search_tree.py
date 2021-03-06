class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # Apply cb to value
    cb(self.value)
    # if both left and right are None then return
    if self.left is None and self.right is None:
      return
    # if left exists, then call depth_first on left
    if self.left is not None:
      self.left.depth_first_for_each(cb)
    # if right exists, then call depth_first on right
    if self.right is not None:
      self.right.depth_first_for_each(cb)

  def breadth_first_for_each(self, cb):
    to_visit = []

    to_visit.append(self)

    while to_visit:
      curr_value = to_visit.pop(0)
      cb(curr_value.value)
      if curr_value.left:
        to_visit.append(curr_value.left)
      if curr_value.right:
        to_visit.append(curr_value.right)


  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
