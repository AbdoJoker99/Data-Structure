import tkinter as tk
from tkinter import messagebox, simpledialog

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class DataStructureApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Structure App")
        
        # Set fixed window size
        self.master.geometry("600x400")
        self.master.resizable(False, False)
        
        # Position the window in the center of the screen
        window_width = 600
        window_height = 400
        
        # Get the screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        
        # Calculate the x and y position for the window to be centered
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        
        # Set the position of the window
        self.master.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')
        
        # Set background color
        self.master.config(bg="#f0f0f0")

        self.selected_structure = tk.StringVar(value="Array")

        self.array = []
        self.stack = []
        self.queue = []
        self.tree_root = None

        self.structure_menu = tk.OptionMenu(
            self.master, self.selected_structure, "Array", "Stack", "Queue", "Tree"
        )
        self.structure_menu.pack(pady=20, padx=10)

        self.show_structure_button = tk.Button(
            self.master, text="Show Selected Data Structure", command=self.show_structure, bg="#4CAF50", fg="white", relief="flat"
        )
        self.show_structure_button.pack(pady=20)

    def show_structure(self):
        selected_structure = self.selected_structure.get()

        if selected_structure == "Array":
            self.show_array_operations()
        elif selected_structure == "Stack":
            self.show_stack_operations()
        elif selected_structure == "Queue":
            self.show_queue_operations()
        elif selected_structure == "Tree":
            self.show_tree_operations()
        else:
            messagebox.showinfo("Data Structure Operation", "Invalid selection")

    def show_array_operations(self):
        self.clear_screen()
        operation_frame = tk.Frame(self.master, bg="#f0f0f0")
        operation_frame.pack(pady=20)

        buttons = [
            ("Insertion", self.insertion_array),
            ("Deletion", self.deletion_array),
            ("Update", self.update_array),
            ("Search", self.search_array),
            ("Traverse", self.traverse_array),
        ]

        for text, command in buttons:
            button = tk.Button(operation_frame, text=text, command=command, bg="#2196F3", fg="white", relief="flat")
            button.pack(side=tk.LEFT, padx=15, pady=5)

        self.add_return_button()

    def show_stack_operations(self):
        self.clear_screen()
        operation_frame = tk.Frame(self.master, bg="#f0f0f0")
        operation_frame.pack(pady=20)

        buttons = [
            ("Push", self.push_stack),
            ("Pop", self.pop_stack),
            ("Traverse", self.traverse_stack),
        ]

        for text, command in buttons:
            button = tk.Button(operation_frame, text=text, command=command, bg="#2196F3", fg="white", relief="flat")
            button.pack(side=tk.LEFT, padx=15, pady=5)

        self.add_return_button()

    def show_queue_operations(self):
        self.clear_screen()
        operation_frame = tk.Frame(self.master, bg="#f0f0f0")
        operation_frame.pack(pady=20)

        buttons = [
            ("Enqueue", self.enqueue_queue),
            ("Dequeue", self.dequeue_queue),
            ("Traverse", self.traverse_queue),
        ]

        for text, command in buttons:
            button = tk.Button(operation_frame, text=text, command=command, bg="#2196F3", fg="white", relief="flat")
            button.pack(side=tk.LEFT, padx=15, pady=5)

        self.add_return_button()

    def show_tree_operations(self):
        self.clear_screen()
        operation_frame = tk.Frame(self.master, bg="#f0f0f0")
        operation_frame.pack(pady=20)

        buttons = [
            ("Insert Node", self.insert_tree_node),
            ("Delete Node", self.delete_tree_node),
            ("Traverse Tree", self.traverse_tree),
        ]

        for text, command in buttons:
            button = tk.Button(operation_frame, text=text, command=command, bg="#2196F3", fg="white", relief="flat")
            button.pack(side=tk.LEFT, padx=15, pady=5)

        self.add_return_button()

    def add_return_button(self):
        return_button = tk.Button(
            self.master, text="Return to Home", command=self.show_home_page, bg="#FF5722", fg="white", relief="flat"
        )
        return_button.pack(pady=20)

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def show_home_page(self):
        self.clear_screen()
        self.__init__(self.master)

    def insertion_array(self):
        item = self.get_user_input("Enter a value:")
        if item:
            self.array.append(item)
            messagebox.showinfo("Array Operation", f"Inserted: {item}")

    def deletion_array(self):
        item = self.get_user_input("Enter a value to delete:")
        if item:
            if item in self.array:
                self.array.remove(item)
                messagebox.showinfo("Array Operation", f"Deleted: {item}")
            else:
                messagebox.showinfo("Array Operation", f"{item} not found in Array")
        else:
            messagebox.showinfo("Array Operation", "Invalid input")

    def update_array(self):
        old_value = self.get_user_input("Enter the value to update:")
        if old_value:
            if old_value in self.array:
                new_value = self.get_user_input("Enter the new value:")
                if new_value is not None:
                    self.array[self.array.index(old_value)] = new_value
                    messagebox.showinfo(
                        "Array Operation", f"Updated: {old_value} to {new_value}"
                    )
            else:
                messagebox.showinfo("Array Operation", f"{old_value} not found in Array")
        else:
            messagebox.showinfo("Array Operation", "Invalid input")

    def search_array(self):
        item = self.get_user_input("Enter a value to search:")
        if item in self.array:
            index = self.array.index(item)
            messagebox.showinfo("Array Operation", f"Found: {item} at index {index}")
        else:
            messagebox.showinfo("Array Operation", f"{item} not found in Array")

    def traverse_array(self):
        traversal_str = ", ".join(str(item) for item in self.array)
        if not traversal_str:
            traversal_str = "Array is empty"
        messagebox.showinfo("Array Operation", f"Array Traversal: {traversal_str}")

    def push_stack(self):
        item = self.get_user_input("Enter a value to push:")
        if item:
            self.stack.append(item)
            messagebox.showinfo("Stack Operation", f"Pushed: {item}")

    def pop_stack(self):
        if self.stack:
            item = self.stack.pop()
            messagebox.showinfo("Stack Operation", f"Popped: {item}")
        else:
            messagebox.showinfo("Stack Operation", "Stack is empty")

    def traverse_stack(self):
        traversal_str = ", ".join(str(item) for item in self.stack)
        if not traversal_str:
            traversal_str = "Stack is empty"
        messagebox.showinfo("Stack Operation", f"Stack Traversal: {traversal_str}")

    def enqueue_queue(self):
        item = self.get_user_input("Enter a value to enqueue:")
        if item:
            self.queue.append(item)
            messagebox.showinfo("Queue Operation", f"Enqueued: {item}")
        else:
            messagebox.showinfo("Queue Operation", "Invalid input")

    def dequeue_queue(self):
        if self.queue:
            item = self.queue.pop(0)
            messagebox.showinfo("Queue Operation", f"Dequeued: {item}")
        else:
            messagebox.showinfo("Queue Operation", "Queue is empty")

    def traverse_queue(self):
        traversal_str = ", ".join(str(item) for item in self.queue)
        if not traversal_str:
            traversal_str = "Queue is empty"
        messagebox.showinfo("Queue Operation", f"Queue Traversal: {traversal_str}")

    def insert_tree_node(self):
        value = self.get_user_input("Enter a value for the new node:")
        if value is not None:
            value = int(value)
            if self.tree_root:
                self.insert_node(self.tree_root, value)
                messagebox.showinfo("Tree Operation", f"Inserted: {value}")
            else:
                self.tree_root = TreeNode(value)
                messagebox.showinfo("Tree Operation", f"Tree created with root value: {value}")

    def insert_node(self, root, value):
        if value < root.value:
            if root.left is None:
                root.left = TreeNode(value)
            else:
                self.insert_node(root.left, value)
        else:
            if root.right is None:
                root.right = TreeNode(value)
            else:
                self.insert_node(root.right, value)

    def delete_tree_node(self):
        value = self.get_user_input("Enter a value to delete from the tree:")
        if value is not None:
            value = int(value)
            if self.tree_root:
                self.tree_root = self.delete_node(self.tree_root, value)
                messagebox.showinfo("Tree Operation", f"Deleted: {value}")
            else:
                messagebox.showinfo("Tree Operation", "Tree is empty")

    def delete_node(self, root, value):
        if root is None:
            return root

        if value < root.value:
            root.left = self.delete_node(root.left, value)
        elif value > root.value:
            root.right = self.delete_node(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.value = self.find_min_value(root.right)
            root.right = self.delete_node(root.right, root.value)

        return root

    def find_min_value(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.value

    def traverse_tree(self):
        if self.tree_root:
            result = []
            self.inorder_traversal(self.tree_root, result)
            messagebox.showinfo(
                "Tree Operation", f"Inorder Traversal: {', '.join(map(str, result))}"
            )
        else:
            messagebox.showinfo("Tree Operation", "Tree is empty")

    def inorder_traversal(self, node, result_list):
        if node:
            self.inorder_traversal(node.left, result_list)
            result_list.append(node.value)
            self.inorder_traversal(node.right, result_list)

    def get_user_input(self, prompt):
        value = simpledialog.askstring("Input", prompt)
        return value


if __name__ == "__main__":
    root = tk.Tk()
    app = DataStructureApp(root)
    root.mainloop()
