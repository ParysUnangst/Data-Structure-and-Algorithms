class TextOperation:
    def __init__(self, operation_type, character=None):
        # Initialize the operation with its type ('add' or 'delete') and the character involved (if applicable)
        self.operation_type = operation_type
        self.character = character

class SimpleTextEditor:
    def __init__(self):
        # Initialize the text editor with an empty text string and an empty operations stack
        self.text = ""
        self.operations_stack = []

    def add_text(self, char):
        # Add the character to the text
        self.text += char
        # Record the add operation on the stack
        self.operations_stack.append(TextOperation('add', char))
        # Display the current state of the text
        self.display_text()

    def delete_text(self):
        # Check if there is any text to delete
        if self.text:
            # Get the last character in the text
            char = self.text[-1]
            # Remove the last character from the text
            self.text = self.text[:-1]
            # Record the delete operation on the stack
            self.operations_stack.append(TextOperation('delete', char))
            # Display the current state of the text
            self.display_text()
        else:
            print("No text to delete")

    def undo(self):
        # Check if there are any operations to undo
        if self.operations_stack:
            # Get the last operation from the stack
            last_operation = self.operations_stack.pop()
            # If the last operation was an add, remove the last character from the text
            if last_operation.operation_type == 'add':
                self.text = self.text[:-1]
            # If the last operation was a delete, add the character back to the text
            elif last_operation.operation_type == 'delete':
                self.text += last_operation.character
            # Display the current state of the text
            self.display_text()
        else:
            print("No operations to undo")

    def display_text(self):
        # Print the current state of the text
        print(f"Current Text: '{self.text}'")

# Example usage
editor = SimpleTextEditor()
editor.add_text('a')  # Adds 'a' to the text
editor.add_text('b')  # Adds 'b' to the text
editor.add_text('c')  # Adds 'c' to the text
editor.delete_text()  # Deletes the last character ('c')
editor.undo()         # Undoes the delete operation, adding 'c' back
editor.undo()         # Undoes the add operation, removing 'c'
editor.undo()         # Undoes the add operation, removing 'b'
editor.undo()         # This should indicate that there's no operation to undo
