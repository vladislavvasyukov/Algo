def insert_fixup(self, z):
    while z.parent.is_red():
        if z.parent.is_left_child():
            y = z.parent.parent.right
            if y.is_red():
                z.parent.set_black()
                y.set_black()
                z.parent.parent.set_red()
            else:
                if z.is_right_child():
                    z = z.parent
                    self.left_rotate(z)
                z.parent.set_black()
                z.parent.parent.set_red()
                self.right_rotate(z.parent.parent)
        else:
            ...


    self.root.set_black()
